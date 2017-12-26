#01 Windows安装Tensorflow

1. 安装Python。

[点击此处](https://www.python.org/downloads/release/python-352/)下载Python3.5.2。安装Python时一定要选择安装pip。

2. 配置Python环境变量。

将%安装路径%\Scripts添加到Path下面。

3. 修改Pip国内源。

在C:\Users\l{你的用户名}\AppData\Local下面创建pip文件夹，在pip文件夹中新建pip.conf文件，写入以下内容。

```conf
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install] 
trusted-host=mirrors.aliyun.com  
```

4. 安装Tensorflow。

打开PowerShell，执行以下代码。

```bash
pip install --upgrade tensorflow
```

5. 测试安装。

打开Python IDLE，输入`import tensorflow as tf`，运行。如果不报错，证明安装成功。
