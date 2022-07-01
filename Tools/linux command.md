# LINUX command

* 打包：

        tar -czf small.tar.gz pdbfiles/
        tar -czf file_name.tar.gz file_name
        tar -xvf file_name.tar
        ref：https://www.pendrivelinux.com/how-to-open-a-tar-file-in-unix-or-linux/

* nohug

        nohup ./batch_download.sh -f log_file.txt -c
        
        #see it works
        ps -aux | grep "./batch_download.sh"   

* 文件个数

        ls -l |grep "^-"|wc -l


* 版本查询

        cat /etc/*-release

* ubuntu

        lsb_release -a
        
        :
        (base) root@87s3gp5rif1k0-0:~# lsb_release -a
        No LSB modules are available.
        Distributor ID: Ubuntu
        Description:    Ubuntu 18.04.5 LTS
        Release:        18.04
        Codename:       bionic

* cenos


        rpm -q centos-linux-release $ rpm -q centos-release

        :
        (base) [kangqiyue@a100 kqy]$ rpm -q centos-linux-release $ rpm -q centos-release
        package centos-linux-release is not installed
        package $ is not installed
        rpm-4.14.2-37.el8.x86_64
        centos-release-8.2-2.2004.0.1.el8.x86_64

        https://linuxpip.org/fix-apt-get-command-not-found/
        https://itsfoss.com/unable-to-locate-package-error-ubuntu/

        