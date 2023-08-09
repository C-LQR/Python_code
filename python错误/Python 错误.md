# Python 错误

## pyinstaller库 打包源文件失败

```
命令行：
C:\Users\25373>pyinstaller -F fly.py
...
PermissionError: [Errno 13] Permission denied: 'C:\\Users\\25373\\AppData\\Local\\pyinstaller\\bincache00_py38_64bit\\ucrtbase.dll
```



## 解决方法：

- **==方法1==：关闭360管家，关闭编译文件，关闭相应文件夹（不见效）**
- **==方法2==：将源文件所在本地路径改为英文字符”C:\Users\25373\Desktop\mai_fly\fly.py“（不见效）**
- **==方法3==：以管理员身份运行cmd，*R+windows, shift+ctrl+enter*（不见效） **

```
命令行：
C:\WINDOWS\system32>pyinstaller -F C:\Users\25373\Desktop\mai_fly\fly.py
...
PermissionError: [Errno 13] Permission denied
```

- **==方法4==：将”C:\Users\25373\AppData\Local\pyinstaller\bincache00_py38_64bit“文件夹-属性-取消只读(仅应用于文件夹中的文件)(不见效)**

![](https://lqr-1317479009.cos.ap-shanghai.myqcloud.com/1.JPG)

取消勾选”只读(仅应用于文件夹中的文件)“,点击确定，

弹出如下对话框”确定属性更改“

![](https://lqr-1317479009.cos.ap-shanghai.myqcloud.com/2.JPG)

点击确定后，文件夹-属性-只读(仅应用于文件夹中的文件) 依旧被勾选着

![](https://lqr-1317479009.cos.ap-shanghai.myqcloud.com/1.JPG)

- **==方法4==：卸载pyinstaller库，重新安装pyinstaller库（不见效）**

​	**卸载pyinstaller库**

```
命令行：
C:\Users\25373>pip uninstall pyinstaller
...
Proceed (Y/n)? y
  Successfully uninstalled pyinstaller-5.7.0
```

​	**安装pyinstaller库**

```
命令行：
C:\Users\25373>pip install pyinstaller
...
Successfully installed pyinstaller-5.9.0
```



## 未来的打算

卸载python，重新安装python到c盘，第三方库重新安装

