# Python、IDLE、IDE、Anaconda的之间的关系

## Python

- 介绍

  **Python**是一门**计算机编程语言**，按照计算机编程语言分类，它属于**解释型语言**，解释型语言又叫脚本语言。
  
  最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，被用于独立的、大型项目的开发。我们在[Python官网](https://www.python.org/)上下载安装的**Python程序**是：**Python解释器[^01]** + **Python虚拟机[^02]**

![](https://lqr-1317479009.cos.ap-shanghai.myqcloud.com/python-icon.png)



- 运行Python代码

  我们可以使用以下四种方式来运行python代码，前提是我们已经下载并安装好了Python程序，配置好其系统**环境变量**[^03]。



1. 在命令窗口运行

   快捷键 Win+ R —> 输入cmd 到命令窗口—> 命窗口内输入python,就可以运行python程序了。

   ![](https://lqr-1317479009.cos.ap-shanghai.myqcloud.com/%E5%91%BD%E4%BB%A4%E7%AA%97%E5%8F%A3.JPG)





2. 脚本方式运行

   新建一个’‘12.txt’‘脚本文件，写完脚本后，然后把名称后缀命名为.py，在命令窗口执行代码 `python x:\xx\xx.py`，填写python文件绝对路径而非相对路径，就可以运行了。

   ![](https://lqr-1317479009.cos.ap-shanghai.myqcloud.com/%E8%84%9A%E6%9C%AC.JPG)

​		







3. 使用Python程序自带的IDLE编辑器

   IDLE是Python自带的编辑器，是迷你版的IDE，与以上方式不同的是它带有图形界面，有简单的编辑和调试功能。同时支持命令窗口运行和脚本文件运行。打开方式：在任务框的搜索栏输入IDLE

   ![](https://lqr-1317479009.cos.ap-shanghai.myqcloud.com/IDLE.JPG)



4. 使用第三方的Python的IDE(集成开发环境)

   第三方的Python的IDE相对于Python自带的IDLE而言，功能更加全面，界面更加美观，操作起来更加容易。目前比较流行的有VScode、PyCharm、Jupyter等。

   

	## IDLE

- 介绍

  IDLE是Python程序 自带的编辑器，是迷你版的IDE



## IDE

- 介绍

  IDE是指计算机程序设计语言的集成开发环境，不止Python有IDE，其他语言也有。集成开发环境包括有：编辑器+调试+语法高亮+Project管理+代码跳转+智能提示+自动完成+单元测试 等功能。==（注意：Python IDE不包括Python程序，但可以调用本地Python程序）==

  

- Python IDE

  目前比较流行的有VScode、PyCharm、Jupyter等



## Anaconda

- 介绍

  Anaconda是一款软件，包括 Python程序 + conda[^03] + 一大堆安装好的工具包比如：numpy**、**pandas等。当然如果只需要某些包或者节省存储空间，可以下载安装Miniconda（Anaconda有mini版本），包括：Python程序 + conda

  ![](https://lqr-1317479009.cos.ap-shanghai.myqcloud.com/anaconda2.jpg)
  
  











[学习python你必须弄懂的 Python、Pycharm、Anaconda 三者之间的关系 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/142657444)

[(9 封私信) 脚本语言是什么？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/419301716/answer/1452610873)

[什么是脚本语言？为什么python是脚本语言？而C和JAVA不是？ 图解解释型语言和编译型语言区别 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/461684569)

[掌握Shell编程，一篇就够了 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/102176365)



[^01]:将Python源文件（xxx.py）解释成二进制码
[^02]:（Python Virtual Machine）一种是高级语言虚拟机，可以模拟硬件来运行二进制码，以消除语言对具体硬件的依赖
[^03]:conda是一个开源的包、环境管理器，可以用于在同一个机器上安装不同版本的Python程序，并能够在不同的环境之间切换。



Script即脚本，原义是手稿。

在电影行业领域，Script指代戏剧表演或电影、电视摄制等所依据的剧本；

在计算机领域，Script指那种可直接运行的文本文件。

能够写出Script的语言，比如Python、Bash、PerlRuby、Groovy等，叫做脚本语言，又叫解释型语言；

用C、C++、Golang、Rust等语言写出的文本文件，需要编译成二进制机器码文件才能运行，所以这类语言称为编译型语言。