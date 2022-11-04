# conda环境相关操作


## conda creat env 
        #conda 创建环境，修改test为其它名字
        conda create --name test python=3.8 -y

        #激活已创建环境
        conda activate test

        #deactivate环境
        conda deactivate

        #conda删除环境
        conda remove --name 环境名称 --all

## jupyter notebook：ipykernel


        #安装ipykernel（为了使jupyter识别）
        conda install ipykernel

        #使该环境在jupyter中显示
        python -m ipykernel install --user --name 环境名称 --display-name "jupyter中显示名称"

        # 查看当前的所有kernel
        jupyter kernelspec list

        # 删除jupyter notebook的kernel
        jupyter kernelspec remove kernelname

## 查看所有环境

        #conda所有环境
        conda env list


## 环境导出和导入

        #导出
        conda env export > environment.yml

        #yml环境导入_1
        conda activate env_name
        conda env update --file environment.yml --prune

        yml环境导入_2
        conda env update --name myenv --file environment.yml --prune

## Miniconda 一键安装&配置国内源

```
#!/usr/bin/bash
set -e
wget "https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh" -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/.miniconda
~/.miniconda/bin/conda init
echo 'Successfully installed miniconda...'
echo -n 'Conda version: '
~/.miniconda/bin/conda --version
echo -e '\n'
exec bash
```

