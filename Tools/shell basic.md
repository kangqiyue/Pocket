## date
```shell
(base) [kangqiyue@a100 ~]$ date
Thu Aug 18 12:54:01 CST 2022
```
## sys path
```shell
base) [kangqiyue@a100 ~]$ echo $PATH
/data/users/kangqiyue/.miniconda/bin:/data/users/kangqiyue/.miniconda/condabin:/data/users/kangqiyue/.local/bin:/data/users/kangqiyue/bin:/usr/local/Modules/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin
```
## path
shell 中的路径是一组被分割的目录，

- Linux 和 macOS 上使用 / 分割，
- Windows上是 \。
- 路径 / 代表的是系统的根目录
- . 表示的是当前目录，而 .. 表示上级目录
## 其它
```shell
ls
pwd
cd
tldr
man ls
```
## 输入流和输出流
最简单的重定向是 < file 和 > file。这两个命令可以将程序的输入输出流分别重定向到文件：
```shell
(base) [kangqiyue@a100 test]$ echo hello > hello.txt
(base) [kangqiyue@a100 test]$ cat hello.txt 
hello
(base) [kangqiyue@a100 test]$ cat < hello.txt
hello
(base) [kangqiyue@a100 test]$ cat < hello.txt > hello2.txt
(base) [kangqiyue@a100 test]$ cat hello2.txt 
hello
```
## >> 和 |

- 使用 >> 来向一个文件追加内容。
- 使用管道（ pipes ），我们能够更好的利用文件重定向。 | 操作符允许我们将一个程序的输出和另外一个程序的输入连接起来


### 将shell转化成pycharm debug参数
> cat test.sh | sed 's/\\//'

