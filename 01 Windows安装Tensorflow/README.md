1��**��װPython��**

[����˴�](https://www.python.org/downloads/release/python-352/)����Python3.5.2����װPythonʱһ��Ҫѡ��װpip��

2��**����Python����������**

��%��װ·��%\Scripts��ӵ�Path���档

3��**�޸�Pip����Դ��**

��C:\Users\l{����û���}\AppData\Local���洴��pip�ļ��У���pip�ļ������½�pip.conf�ļ���д���������ݡ�

<pre>
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install] 
trusted-host=mirrors.aliyun.com  
</pre>

**4����װTensorflow��**

��PowerShell��ִ�����´��롣

<pre>
pip install --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-0.12.0rc1-cp35-cp35m-win_amd64.whl
</pre>

����İ�װ����װ��Windows��Tensorboard�޷���ʾ�κ����ݣ�����ʹ������İ�װ����װ��

<pre>
pip install --upgrade http://ci.tensorflow.org/view/Nightly/job/nightly-win/DEVICE=cpu,OS=windows/lastSuccessfulBuild/artifact/cmake_build/tf_python/dist/tensorflow-0.12.1-cp35-cp35m-win_amd64.whl
</pre>

**5�����԰�װ��**

��Python IDLE������import tensorflow as tf�����С����������֤����װ�ɹ���

6��**�ο����ϡ�**

��ԭ��Windows��װTensorflow0.12�ķ�������[http://blog.csdn.net/include1224/article/details/53452824](http://blog.csdn.net/include1224/article/details/53452824)

**ע�����**

1��ʹ�òο������еİ���װ��Tensorflow�����е�TensorBoard����Windows���޷�������ʾ����������ȱ����Դ����ԭ�����������[https://github.com/tensorflow/tensorflow/issues/5983](https://github.com/tensorflow/tensorflow/issues/5983)���ٷ������Ľ�����������°汾������ǰ��ʹ��[http://ci.tensorflow.org/view/Nightly/job/nightly-win/](http://ci.tensorflow.org/view/Nightly/job/nightly-win/)�İ汾��װ��rc0��rc1������������⡣