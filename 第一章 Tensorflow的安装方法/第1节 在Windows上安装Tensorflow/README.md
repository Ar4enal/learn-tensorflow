# 第一节 在Windows上安装Tensorflow

1. 安装Python。

[点击此处](https://www.python.org/downloads/release/python-352/)下载Python3.5.2，然后安装。

2. 配置Python环境。

在Windows上安装Python，默认是自动添加环境变量的。如果没有，可以把`%安装路径%\Scripts`添加到`Path`环境变量中。

3. 修改pip源。

在国内，通过pip安装软件包是很慢的，还经常中断。你可以在`C:\Users\{你的用户名}\AppData\Local`目录下创建一个名称是`pip`的文件夹，然后在文件夹中创建一个名为`pip.conf`的文件，在里面输入以下内容。这样你就把pip源切换到阿里云了。

```conf
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install] 
trusted-host=mirrors.aliyun.com  
```

4. 安装Tensorflow。

安装CPU版Tensorflow比较简单，直接用pip安装即可。但是安装GPU版Tensorflow比较复杂，首先你得有个Nvdia的显卡（例如GTX960，GTX1080等），还得安装CUDA和CUDNN，好处是速度快，训练比较复杂的网络（例如卷积神经网络）比CPU版快百倍。

**安装CPU版Tensorflow**

打开`PowerShell`，如果你想安装CPU版的Tensorflow，输入以下代码即可。

```bash
pip install tensorflow
```

*安装GPU版Tensorflow*

如果你电脑上有Nvdia的显卡（例如GTX960、GTX1080等），你可以安装GPU版的Tensorflow。GPU版的Tensorflow比CPU版的快百倍。首先输入以下代码。

```bash
pip install tensorflow-gpu
```

然后打开Python解释器，输入`import tensorflow`，这时它会提示你缺少的CUDA。根据它的提示在`https://developer.nvidia.com/cuda-downloads`下载对应版本的CUDA并安装。

然后再次打开Python解释权，输入`import tensorflow`，这时它会提示你缺少的CUDNN版本。根据提示在`https://developer.nvidia.com/cudnn`下载对应版本的CUDNN，可能需要注册。

注意：每个Tensorflow对应的CUDA版本和CUDNN版本都不一样，最好是先安装Tensorflow，然后根据它的提示选择对应的版本。

5. 测试安装。

打开Python解释器，输入`import tensorflow as tf`并执行。如果没有错误，那么恭喜你成功安装Tensorflow。