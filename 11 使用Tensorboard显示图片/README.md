���ȣ�����һ��png��ʽ��ͼƬ��ע�⣺ֻ֧��png��ʽ��������Ϊ1.png��Ȼ�󣬴�PythonShell���������´��룺
  
<pre>
import tensorflow as tf

# ��ȡͼƬ����
file = open('1.png', 'rb')
data = file.read()
file.close()

# ͼƬ����
image = tf.image.decode_png(data, channels=4)
image = tf.expand_dims(image, 0)

# ��ӵ���־��
sess = tf.Session()
writer = tf.summary.FileWriter('logs')
summary_op = tf.summary.image("image1", image)

# ���в�д����־
summary = sess.run(summary_op)
writer.add_summary(summary)

# �ر�
writer.close()
sess.close()
  
</pre>

Ȼ������ͬĿ¼��cmd������tensorboard --logdir=logs��Ȼ������������http://localhost:6006/����Tensorboard��Images��ǩҳ���Ϳ��Կ������ǵ�pngͼƬ�ˡ�

�ο����ϣ���Tensorflow: How to Display Custom Images in Tensorboard (e.g. Matplotlib Plots)����[http://stackoverflow.com/questions/38543850/tensorflow-how-to-display-custom-images-in-tensorboard-e-g-matplotlib-plots](http://stackoverflow.com/questions/38543850/tensorflow-how-to-display-custom-images-in-tensorboard-e-g-matplotlib-plots)