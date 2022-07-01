# Introduction of bash and sh

## note on linux command and bash
Bash is the shell, a text mode user interface, in which the Linux commands are typed. Bash will then launch them. Without such an interface, it would be impossible to launch these commands.

The Linux command, are not Linux but GNU commands. Linux is the kernel of the system. The commands, the bash shell and many other parts of the system, are part of the GNU projec

===

Linux是系统的内核，Linux命令属于GNU命令的一部分。

Bash是shell，一个文本模式的用户界面，在其中可以键入Linux命令。然后Bash将启动它们。如果没有这样的界面，就不可能启动这些命令。Linux命令、bash shell和系统的许多其他部分，都是GNU项目的一部分。

ref: https://www.quora.com/Are-Linux-command-and-bash-the-same-thing

---
## note on bash and sh

bash and sh are two different shells of the Unix operating system. bash is sh, but with more features and better syntax. Bash is “Bourne Again SHell”, and is an improvement of the sh (original Bourne shell). Shell scripting is scripting in any shell, whereas Bash scripting is scripting specifically for Bash. sh is a shell command-line interpreter of Unix/Unix-like operating systems. sh provides some built-in commands. bash is a superset of sh. Shell is a command-line interface to run commands and shell scripts. Shells come in a variety of flavors, much as operating systems come in a variety of flavors. So, Shell is an interface between the user and the operating system, which helps the user to interact with the device.

===

bash和sh 是两种不同的unix类系统的shell。Bash is “Bourne Again SHell”, sh is the original Bourne shell.

bash包括sh，但是具有更多功能和语法。

sh is a shell command-line interpreter（for Unix/Unix-like operating systems）；而且提供了一些内置命令。

shell是运行command，shell脚本的command-line interface，Shell有多种，Shell 是用户与操作系统之间的接口，它帮助用户与设备进行交互。


**Difference between sh and bash:** 
|                        bash                       |                  sh                       |
|:-------------------------------------------------:|:-----------------------------------------:|
| Bourne Again SHell                                | SHell                                     |
| Developed by Brain Fox                            | Developed by Stephen R. Bourne            |
| Successor of sh                                   | Predecessor of bash                       |
| bash is the default SHELL                         | sh is the not default SHELL               |
| #!/bin/bash                                       | #!/bin/sh                                 |
| It has more Functionality with up-gradation.      | It has less functionality.                |
| supports job controls.                            | does not support job control.             |
| bash is not a valid POSIX shell.                  | sh is a valid POSIX shell.                |
| Easy to use                                       | not as easy as bash                       |
| less portable than sh.                            | more portable than bash.                  |
| Extended version of language                      | Original language                         |
| Bash scripting is scripting specifically for Bash | Shell scripting is scripting in any shell |
| supports command history.                         | does not supports command history.        |


ref: https://www.geeksforgeeks.org/difference-between-sh-and-bash/#:~:text=bash%20and%20sh%20are%20two,is%20scripting%20specifically%20for%20Bash.

---
## note on vim
Vim是Unix及类Unix系统文本编辑器。Vim是一个类似于Vi的著名的功能强大、高度可定制的文本编辑器，在Vi的基础上改进和增加了很多特性。VIM是自由软件。Vim普遍被推崇为类Vi编辑器中最好的一个。大多数 UNIX系统和Apple OS-X都将Vim作为“vi”包含在内。

Vim is a free and open-source, screen-based text editor program for Unix.

ref: https://aliarefwriorr.medium.com/what-is-vim-2d5a6aa6a787

---
## 查看shell

### 当前使用的shell（linux默认bash）

        grep $USER /etc/passwd
        ******:/bin/bash

### 查看已安装的shell
        cat /etc/shells

        >
        /bin/sh
        /bin/bash
        /usr/bin/sh
        /usr/bin/bash
        /usr/bin/zsh
        /bin/zsh

ref： https://www.baeldung.com/linux/sh-vs-bash

