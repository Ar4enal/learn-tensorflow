# 第3节 安装Tensorboard

Tensorboard可以可视化查看神经网络和神经网络的训练过程。

1. 打开`PowerShell`或者`Shell`，输入`pip install tensorboard`即可。

2. 你可以输入`pip show tensorboard`获取Tensorboard的安装路径。

例如，在Ubuntu上， 

```bash
liteng@Lenovo-G470:~$ pip show tensorboard
Name: tensorboard
Version: 1.0.0a6
Summary: Standalone TensorBoard for visualizing in deep learning
Home-page: https://github.com/dmlc/tensorboard
Author: zihaolucky
Author-email: zihaolucky@gmail.com
License: Apache 2.0
Location: /home/liteng/.local/lib/python3.6/site-packages
Requires: werkzeug, Pillow, six, protobuf, numpy, wheel
```

。很明显，你的Tensorflow安装在`/home/liteng/.local/lib/python3.6/site-packages`目录下。

2. 输入以下代码，可以启动Tensorboard，注意Tensorboard和日志文件的争取路径。

```bash
python ~/.local/lib/python3.6/site-packages/tensorboard/main.py --logdir=logs
```

如果你看到，

```
TensorBoard 0.4.0rc3 at http://Lenovo-G470:6006 (Press CTRL+C to quit)
```

，那么你成功启动了Tensorboard。你可以在浏览器中输入`http://localhost:6006`查看Tensorboard。