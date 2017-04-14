�����룺

<pre>
import tensorflow as tf
import numpy as np

# �����������ݣ����������������x_data��y_data֮��Ĺ�ϵ��
x_data = np.linspace(-1,1,300)[:, np.newaxis] # -1��1�ȷ�300���γɵĶ�ά����
noise = np.random.normal(0,0.05, x_data.shape) # ��������״ͬx_data��0-0.05������̬�ֲ���С��
y_data = np.square(x_data)-0.5+noise # x_dataƽ������0.05���ټ�����ֵ

# ����㣨1����Ԫ��
xs = tf.placeholder(tf.float32, [None, 1]) # ռλ����None��ʾn*1ά��������n��ȷ��
ys = tf.placeholder(tf.float32, [None, 1]) # ռλ����None��ʾn*1ά��������n��ȷ��

# ���㣨10����Ԫ��
W1 = tf.Variable(tf.random_normal([1,10])) # Ȩ�أ�1*10�ľ��󣬲��÷�����̬�ֲ�����������
b1 = tf.Variable(tf.zeros([1,10])+0.1) # ƫ�ã�1*10�ľ���ʹ��0.1���
Wx_plus_b1 = tf.matmul(xs,W1) + b1 # ����xs��W1��ˣ�Ȼ�����ƫ��
output1 = tf.nn.relu(Wx_plus_b1) # �����ʹ��tf.nn.relu

# ����㣨1����Ԫ
W2 = tf.Variable(tf.random_normal([10,1]))
b2 = tf.Variable(tf.zeros([1,1])+0.1)
Wx_plus_b2</span> = tf.matmul(output1,W2) + b2
output2 = Wx_plus_b2

# ��ʧ
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-output2),reduction_indices=[1])) # �ڵ�һά�ϣ�ƫ��ƽ������ͣ�����ƽ��ֵ����������ʧ
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss) # ʹ���ݶ��½��������ò���0.1������С����ʧ

# ��ʼ��
init = tf.global_variables_initializer() # ��ʼ�����б���
sess = tf.Session()
sess.run(init) # ������ʼ��

# ѵ��
for i in range(1000): #ѵ��1000��
��_,loss_value = sess.run([train_step,loss],feed_dict={xs:x_data,ys:y_data}) # �����ݶ��½����㣬������ÿһ������ʧ
��if(i%50==0):
����print(loss_value) # ÿ50�����һ����ʧ
</pre>

</div>

�����

0.405348
0.00954485
0.0068925
0.00551958
0.00471453
0.00425206
0.00400382
0.00381883
0.00367445
0.00353349
0.00341325
0.00330487
0.00321128
0.00313468
0.0030646
0.0030014
0.00294802
0.00290179
0.0028618
0.00282344

���Կ��������ѵ���Ľ��У���ʧԽ��ԽС��֤�����Խ��Խ�á�

�ο����ϣ�

��Tensorflow �Դ����ӻ�Tensorboardʹ�÷��� ����Ŀ���롷��[http://blog.csdn.net/jerry81333/article/details/53004903](http://blog.csdn.net/jerry81333/article/details/53004903)

��tensorflowѧϰ��������tensorflow�е�tf.reduce_mean()���ຯ������[http://blog.csdn.net/qq_32166627/article/details/52734387](http://blog.csdn.net/qq_32166627/article/details/52734387)