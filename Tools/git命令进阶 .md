# git stash
#### push到stash中，指定名字为my_stash
> git stash push -m "my_stash" 

#### 列出所有stash
> git stash list 
> ![image.png](https://cdn.nlark.com/yuque/0/2022/png/22331600/1661316899707-dec601e1-a479-49bd-81fc-42238cd35d39.png#clientId=u1a7f9e0d-04d1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=81&id=u4202bae0&margin=%5Bobject%20Object%5D&name=image.png&originHeight=126&originWidth=839&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27912&status=done&style=none&taskId=u49744725-b1bc-4594-928d-cecccd6ab51&title=&width=537.8888854980469)

#### pop出某个指定stash，删除该记录

- To apply a stash and remove it from the stash stack, type:
> git stash pop stash@{n} 

#### apply stash，但是保留保存的记录；

- 使用编号
- To apply a stash and keep it in the stash stack, type:
> git stash apply 1
> git stash apply stash@{n} 

#### apply stash；使用name

- Notice that you can apply a stash and keep it in the stack by using the stash name:
> git stash apply my_stash_name

ref： [https://stackoverflow.com/questions/11269256/how-to-name-and-retrieve-a-stash-by-name-in-git](https://stackoverflow.com/questions/11269256/how-to-name-and-retrieve-a-stash-by-name-in-git)
# 分支：git  branch
分支是使用 Git 工作的一个重要部分。你做的任何提交都会发生在当前“checked out”到的分支上。使用 git status 查看那是哪个分支。
### 创建分支
> $ git branch [branch-name]
> 创建一个新分支


> $ git switch -c [branch-name]
> 切换到指定分支并更新工作目录(working directory)

### 其它分支历史合并到当前分支
> $ git merge [branch]
> 将指定分支的历史合并到当前分支。这通常在拉取请求(PR)中完成，但也是一个重要的 Git 操作。

### 删除指定分支

- 删除本地分支：
>  		git branch -d master

- 删除远程分支：
> git push origin -d master

- The -d option is an alias for --delete, which only deletes the branch if it has already been fully merged in its upstream branch.
- The -D option is an alias for --delete --force, which deletes the branch "irrespective of its merged status." [Source: man git-branch]

# 创建仓库：git init；git clone
当着手于一个新的仓库时，你只需创建一次。要么在本地创建，然后推送到 GitHub；要么通过 clone 一个现有仓库。
## git init
> $ git init
> 在使用过 git init 命令后，使用以下命令将本地仓库与一个 GitHub 上的空仓库连接起来：


> $ git remote add origin [url]
> 将现有目录转换为一个 Git 仓库

## git clone
#### 普通clone
> $ git clone [url]
> Clone（下载）一个已存在于 GitHub 上的仓库，包括所有的文件、分支和提交(commits)

#### 仅克隆，指定的某个branch
> git clone --single-branch --branch qiyue [https://github.com/kangqiyue/DeepGCN-RT.git](https://github.com/kangqiyue/DeepGCN-RT.git)

# 同步更改：fetch；merge；push；pull
将你本地仓库与 GitHub.com 上的远端仓库同步
## git fetch
> $ git fetch
> 下载远端跟踪分支的所有历史

## git merge
> $ git merge
> 将远端跟踪分支合并到当前本地分支

## git push
> $ git push
> 将所有本地分支提交上传到 GitHub

## git pull
> $ git pull
> 使用来自 GitHub 的对应远端分支的所有新提交更新你当前的本地工作分支。git pull 是 git fetch 和 git merge 的结合

# 配置工具：git config
对所有本地仓库的用户信息进行配置

> $ git config --global user.name "[name]"
> 对你的commit操作设置关联的用户名


> $ git config --global user.email "[email address]"
> 对你的commit操作设置关联的邮箱地址


> $ git config --global color.ui auto
> 启用有帮助的彩色命令行输出

# 进行更改：git log
浏览并检查项目文件的发展
> $ git log
> 列出当前分支的版本历史


> $ git log --follow [file]
> 列出文件的版本历史，包括重命名


> $ git diff [first-branch]...[second-branch]
> 展示两个分支之间的内容差异


> $ git show [commit]
> 输出指定commit的元数据和内容变化


> $ git add [file]
> 将文件进行快照处理用于版本控制


> $ git commit -m "[descriptive message]"
> 将文件快照永久地记录在版本历史中


# 术语表

- git: 一个开源的分布式版本控制系统
- GitHub: 一个托管和协作管理 Git 仓库的平台
- commit 提交: 一个 Git 对象，是你整个仓库的快照的哈希值
- branch 分支: 一个轻型可移动的 commit 指针
- clone: 一个仓库的本地版本，包含所有提交和分支
- remote 远端: 一个 GitHub 上的公共仓库，所有小组成员通过它来交换修改
- fork: 一个属于另一用户的 GitHub 上的仓库的副本
- pull request 拉取请求: 一处用于比较和讨论分支上引入的差异，且具有评审、评论、集成测试等功能的地方
- HEAD: 代表你当前的工作目录。使用git checkout 可移动 HEAD 指针到不同的分支、标记(tags)或提交
# 重做提交：git reset
清除错误和构建用于替换的历史
> $ git reset [commit]
> 撤销所有 [commit] 后的的提交，在本地保存更改


> $ git reset --hard [commit]
> 放弃所有历史，改回指定提交。


> 小心！更改历史可能带来不良后果。如果你需要更改 GitHub（远端）已有的提交，请谨慎操作。如果你需要帮助，可访问 [github.community](https://github.community) 或联系支持(support)。

# .gitignore 文件
有时一些文件最好不要用 Git 跟踪。这通常在名为 .gitignore 的特殊文件中完成。你可以在 [github.com/github/gitignore](https://github.com/github/gitignore) 找到有用的 .gitignore 文件模板。
# reference
[https://training.github.com/downloads/zh_CN/github-git-cheat-sheet/](https://training.github.com/downloads/zh_CN/github-git-cheat-sheet/)
# 

