library(dplyr)
getwd()
rm(list = ls())
#setwd
dir <- c("m")
fix(dir)
dir
setwd(dir)
getwd()
dir()


#read data
mydata1 <- read.xlsx(file.choose())
names(mydata1)
mydata1$`索引-correct` <- as.character(mydata1$`索引-correct`)
mydata2 <- read.xlsx(file.choose())

mydata2 <- read.csv(file.choose(), stringsAsFactors = FALSE, header = TRUE)
mydata2$`索引-correct` <- as.character(mydata2$`索引-correct`)
names(mydata2)

mydata2 <- mutate(mydata2, ion_name = paste0(Class, FattyAcid))
mydata3 <- select(mydata2, c("FattyAcid", "Area", "ion_name"))

names(mydata1)
names(mydata2)
left <- left_join(mydata1, mydata2, by = c("索引-correct" = "索引-correct"))

#dplyr join

full <- full_join(mydata1, mydata2, by = c("ID" = "ID"))

inner <- inner_join(mydata1,mydata2, by = c("SR" = "TPHP"))
full <- full_join(mydata1, mydata2, by = c("索引"  = "索引号"))
left <- left_join(mydata1, mydata2, by = c("索引" = "总编号.建档."))
full <- full_join(mydata1, mydata2, by = c("name" = "Ů????260"))
left <- left_join(mydata1, mydata2, by = c("??????" = "?ܱ???"))


full <- full_join(mydata1, mydata2, by = c("name"  = "namescreen"))
#save the result
getwd()
write.csv(inner, "inner.csv")
write.csv(full, "full_join.csv")
write.csv(left, "left.csv")
write.csv(mydata1, "mydata1.csv")
#######################################
quan <- NULL
for (i in 9:ncol(mydata1)) {
        quan_data <- mydata1[ , i]
        quantile <- quantile(quan_data) %>% as.data.frame()
        detection <- sum(quan_data > 0)
        quantile <- t(quantile)
        quan0 <- cbind(colnames(mydata1)[i], detection, quantile)
        quan <- rbind(quan, quan0)

}
write.csv(quan, "SERUM.quan.csv")
##########################################
