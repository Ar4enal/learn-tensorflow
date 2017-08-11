1、**安装Python。**

[点击此处](https://www.python.org/downloads/release/python-352/)下载Python3.5.2。安装Python时一定要选择安装pip。

2、**配置Python环境变量。**

将%安装路径%\Scripts添加到Path下面。

3、**修改Pip国内源。**

在C:\Users\l{你的用户名}\AppData\Local下面创建pip文件夹，在pip文件夹中新建pip.conf文件，写入以下内容。

<pre>
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install] 
trusted-host=mirrors.aliyun.com  
</pre>

**4、安装Tensorflow。**

打开PowerShell，执行以下代码。

<pre>
pip install --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-0.12.0rc1-cp35-cp35m-win_amd64.whl
</pre>

上面的安装包安装后，Windows下Tensorboard无法显示任何数据，可以使用下面的安装包安装。

<pre>
pip install --upgrade http://ci.tensorflow.org/view/Nightly/job/nightly-win/DEVICE=cpu,OS=windows/lastSuccessfulBuild/artifact/cmake_build/tf_python/dist/tensorflow-0.12.1-cp35-cp35m-win_amd64.whl
</pre>

**5、测试安装。**

打开Python IDLE，输入import tensorflow as tf，运行。如果不报错，证明安装成功。

6、**参考资料。**

《原生Windows安装Tensorflow0.12的方法》：[http://blog.csdn.net/include1224/article/details/53452824](http://blog.csdn.net/include1224/article/details/53452824)

**注意事项：**

1、使用参考资料中的包安装的Tensorflow，其中的TensorBoard，在Windows下无法正常显示，这是由于缺少资源包的原因。详情请见：[https://github.com/tensorflow/tensorflow/issues/5983](https://github.com/tensorflow/tensorflow/issues/5983)。官方给出的解决方案是在新版本出来以前，使用[http://ci.tensorflow.org/view/Nightly/job/nightly-win/](http://ci.tensorflow.org/view/Nightly/job/nightly-win/)的版本安装。rc0和rc1都存在这个问题。