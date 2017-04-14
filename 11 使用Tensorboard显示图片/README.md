首先，下载一张png格式的图片（注意：只支持png格式），命名为1.png。然后，打开PythonShell，输入以下代码：
  
<pre>
import tensorflow as tf

# 获取图片数据
file = open('1.png', 'rb')
data = file.read()
file.close()

# 图片处理
image = tf.image.decode_png(data, channels=4)
image = tf.expand_dims(image, 0)

# 添加到日志中
sess = tf.Session()
writer = tf.summary.FileWriter('logs')
summary_op = tf.summary.image("image1", image)

# 运行并写入日志
summary = sess.run(summary_op)
writer.add_summary(summary)

# 关闭
writer.close()
sess.close()
  
</pre>

然后，在相同目录打开cmd，输入tensorboard --logdir=logs，然后打开浏览器输入http://localhost:6006/。在Tensorboard的Images标签页，就可以看到我们的png图片了。

参考资料：《Tensorflow: How to Display Custom Images in Tensorboard (e.g. Matplotlib Plots)》：[http://stackoverflow.com/questions/38543850/tensorflow-how-to-display-custom-images-in-tensorboard-e-g-matplotlib-plots](http://stackoverflow.com/questions/38543850/tensorflow-how-to-display-custom-images-in-tensorboard-e-g-matplotlib-plots)