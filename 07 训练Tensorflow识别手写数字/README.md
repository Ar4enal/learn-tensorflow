��Python Shell���������´��룺

<pre>
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# ��ȡ���ݣ�������ھͶ�ȡ�������ھ��������ٶ�ȡ��
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# ����
x = tf.placeholder("float", [None, 784]) #����ռλ����ÿ����д����784�����ص㣩
y_ = tf.placeholder("float", [None,10]) #����ռλ����������д���־�������ֵ��0-9��Ӧ�����10��λ�ã�

# �������softmax�ὫxW+b�ֳ�10�࣬��Ӧ0-9
W = tf.Variable(tf.zeros([784,10])) #Ȩ��
b = tf.Variable(tf.zeros([10])) #ƫ��
y = tf.nn.softmax(tf.matmul(x,W) + b) # �������x��Ȩ�ؾ���W��ˣ�����ƫ�þ���b��Ȼ����softmax��sigmoid���������棬���Էֳɶ��ࣩ

# ����ƫ���
cross_entropy = -tf.reduce_sum(y_*tf.log(y))

# ʹ���ݶ��½���������0.01������ʹƫ�����С
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# ��ʼ������
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(10): # ѵ��10��
  batch_xs, batch_ys = mnist.train.next_batch(100) # ���ȡ100����д����ͼƬ
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys}) # ִ���ݶ��½��㷨������ֵx��batch_xs������ֵy��batch_ys

# ����ѵ������
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})) #���о���ͼ��x��y_�Ӳ�����дͼƬ��ȡֵ
</pre>

ִ�иöδ��룬���0.8002��ѵ��10�εõ�80.02%��ʶ��׼ȷ�ȣ����ǿ��Եġ�

˵������������ԭ����д����ͼƬ�����޷����أ�����ֱ�����ر������õĳ��������Ѿ���������дͼƬ��Դ��py�ű���

���ӣ�[http://pan.baidu.com/s/1cmYSXK](http://pan.baidu.com/s/1cmYSXK) ���룺va2z

�ο����ϣ�

1�����������ѧϰ��ѧ�ߵ� MNIST �����̡̳���[http://www.tensorfly.cn/tfdoc/tutorials/mnist_beginners.html](http://www.tensorfly.cn/tfdoc/tutorials/mnist_beginners.html)