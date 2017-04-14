���ǵ�ģ��ѵ��������������ã��������ҽ���ѵ�����꣬���������ѵ������ô�죿�����Ҫģ�͵ı������ȡ�������룺

<pre>
import tensorflow as tf
import numpy as np
import os

#��������
x_data = np.linspace(-1,1,300)[:, np.newaxis]
noise = np.random.normal(0,0.05, x_data.shape)
y_data = np.square(x_data)-0.5+noise

#�����
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

#����
W1 = tf.Variable(tf.random_normal([1,10]))
b1 = tf.Variable(tf.zeros([1,10])+0.1)
Wx_plus_b1 = tf.matmul(xs,W1) + b1
output1 = tf.nn.relu(Wx_plus_b1)

#�����
W2 = tf.Variable(tf.random_normal([10,1]))
b2 = tf.Variable(tf.zeros([1,1])+0.1)
Wx_plus_b2 = tf.matmul(output1,W2) + b2
output2 = Wx_plus_b2

#��ʧ
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-output2),reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#ģ�ͱ�����ع���
saver = tf.train.Saver()

#�ж�ģ�ͱ���·���Ƿ���ڣ������ھʹ���
if not os.path.exists('tmp/'):
����os.mkdir('tmp/')

#��ʼ��
sess = tf.Session()
if os.path.exists('tmp/checkpoint'): #�ж�ģ���Ƿ����
����saver.restore(sess, 'tmp/model.ckpt') #���ھʹ�ģ���лָ�����
else:
����init = tf.global_variables_initializer() #�����ھͳ�ʼ������
����sess.run(init)

#ѵ��
for i in range(1000):
����_,loss_value = sess.run([train_step,loss], feed_dict={xs:x_data,ys:y_data})
����if(i%50==0): #ÿ50�α���һ��ģ��
��������save_path = saver.save(sess, 'tmp/model.ckpt') #����ģ�͵�tmp/model.ckpt��ע��һ��Ҫ��һ���ļ��У����򱣴治�ɹ�������
��������print("ģ�ͱ��棺%s ��ǰѵ����ʧ��%s"%(save_path, loss_value))
</pre>

��ҵ�һ��ѵ���õ���

ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��1.35421
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.011808
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00916655
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00690887
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00575491
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00526401
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00498503
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00478226
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.0046346
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00454276
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00446402
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00436883
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00427732
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00418589
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00409241
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00400956
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00392799
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00383506
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00373741
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00366922

�ڶ��μ���ѵ�����õ���

ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00412003
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00388735
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00382827
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00379988
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00378107
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.003764
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00375149
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00374324
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00373386
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00372364
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00371543
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00370875
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00370262
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00369697
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00369161
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00368653
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00368169
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00367714
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00367274
ģ�ͱ��棺tmp/model.ckpt ��ǰѵ����ʧ��0.00366843

���Կ������ڶ���ѵ�����ڵ�һ��ѵ���Ļ����ϼ���ѵ���ġ����ǣ����ǿ��԰�������Ҫ��ģ�ͱ�������������ѵ����

�ο��ĵ���

1����TensorFlowʹ��ָ�ϡ���http://www.tensorfly.cn/tfdoc/tutorials/mnist_tf.html