# ####
# DIA_window = 5
# neutral_mass = 35.9766777#179.9504273
# peak_width = 1
# peak_interval = 15
# file = "D:\\R Project\\DIA\\Fipronil代谢产物\\FipData\\FIP100_150.mzXML"
# # file = "D:\\R Project\\DIA\\FFData\\DIA400_450.mzXML"
# data_centroid <- readMzXmlFile(mzXmlFile =  file)
cat(getwd())
#########################################
scan.info <- sapply(data_centroid, extractInfo)
scan.info <- do.call(rbind.data.frame, scan.info)
result <- NULL
# find the target neutral loss in DIA
pb <- txtProgressBar(style=3)
star_time <- Sys.time()
cat("num1: DNL_peak_picking precess")
for (i in 1:length(data_centroid)) {
        setTxtProgressBar(pb, i/length(data_centroid))
        if(JudgeMS(data_centroid[[i]]) == 2){
                loop_data <- data_centroid[[i]]
                #get info

                m_z <- loop_data$metaData[["precursorMz"]]
                rt <- loop_data$metaData[["retentionTime"]]
                num <- loop_data$metaData[["num"]]
                msLevel <- loop_data$metaData[["msLevel"]]
                precursorMz <- loop_data$metaData$precursorMz
                #spectra
                loop_spectra <- loop_data$spectrum %>%
                        as.data.frame() %>%
                        filter(intensity > 0)
                #find precursor ions ranges in MS2 spectra
                ms2_precursor <- filter(loop_spectra, mass < (m_z + DIA_window) & mass > (m_z - DIA_window))
                #judge if ms2_precursor exists
                if(nrow(ms2_precursor) >= 1){
                        for (j in 1:nrow(ms2_precursor)) {
                                ms2_precursor_loop <- ms2_precursor$mass[j]
                                ms2_ms1_intensity <- ms2_precursor$intensity[j]
                                find_target_ion <- mutate(loop_spectra,
                                                          detla = abs((mass + neutral_mass - ms2_precursor_loop)/ms2_precursor_loop*1000000)) %>%
                                        filter((detla <= 10))

                                length1 <- nrow(find_target_ion)
                                if(length1 >= 1){
                                        find_target_ion <- find_target_ion %>%
                                                arrange(desc(intensity))
                                        ms2 <- find_target_ion[["mass"]][[1]]
                                        ms2_intensity <- find_target_ion[["intensity"]][[1]]
                                        ppm <- find_target_ion$detla[1]
                                        daughterion <- cbind(ms2, ms2_intensity, ms2_precursor_loop, ms2_ms1_intensity,
                                                             rt, num, msLevel, m_z)
                                        result <- rbind(result, daughterion )

                                }

                        }
                }

        }
}

print(getwd())
result <- as.data.frame(result)
write.csv(result, paste0("Neutral_mass_", neutral_mass , "_", min(result$m_z),"_", max(result$m_z), "_peak_picking.csv"))
cat(
        paste0("The following file was generated: Neutral_mass_", neutral_mass , "_", min(result$m_z),"_", max(result$m_z), "_peak_picking.csv")
)

#-----------------------------------
#part 2
#group m/z
###############################
#sort data, import!!!
groupData <- read.csv(
        paste0("Neutral_mass_", neutral_mass , "_", min(result$m_z),"_", max(result$m_z), "_peak_picking.csv"),
        header = TRUE, stringsAsFactors = FALSE) %>%
        mutate(round = round(ms2_precursor_loop, 1)) %>%
        arrange(round, rt)


################################
ppm_group <- NULL
result_ppm_group <- NULL
g <- 1
result_ppm_group <- rbind(result_ppm_group, groupData[1,] %>% mutate(group = g))
for(i in 2:nrow(groupData)){
        detla_ppm <- calppm(groupData$ms2_precursor_loop[i], groupData$ms2_precursor_loop[i-1])
        detla_rt <- abs(groupData$rt[i] - groupData$rt[i-1])
        judgment <- (detla_ppm <= 10)& (detla_rt <= peak_interval)
        if((detla_ppm <= 10)& (detla_rt <= peak_interval)){
                temp_group <- groupData[i,] %>% mutate(group = g)

        }
        else{
                g <- g + 1
                temp_group <- groupData[i,] %>% mutate(group = g)
        }
        result_ppm_group <- rbind(result_ppm_group, temp_group)
}
#######################
#test<- do.call(rbind.data.frame, group_filter)
#split
group_filter <- mutate(result_ppm_group, group_pile = paste0("DNL_",m_z, "_" ,group)) %>%
        group_by(group_pile) %>%
        dplyr::mutate(n = n(), detla_rt = (max(rt) - min(rt))/(n-1) * (n + 2)) %>%
        filter(n >= 3)  %>%
        arrange(group_pile, num) %>%
        ungroup(group_filter)

######################
end_time <- Sys.time()  ## 记录程序结束时间
## 第三个位置关闭进度条
close(pb)
run_time <- end_time - star_time
cat(paste0("run time-1", run_time))
###########33
write.csv(group_filter, paste0("Neutral_mass_", neutral_mass , "_", min(group_filter$m_z),"_", max(group_filter$m_z), "_DNL_group.csv"))

print(
        paste0("The following file was generated: ",
               paste0("Neutral_mass_", neutral_mass , "_",
                      min(group_filter$m_z),"_",
                      max(group_filter$m_z),
                      "_DNL_group.csv"))
)

data_DNL <- read.csv(
        paste0("Neutral_mass_", neutral_mass , "_", min(group_filter$m_z),"_", max(group_filter$m_z), "_DNL_group.csv"),
        header = TRUE, stringsAsFactors = FALSE)

