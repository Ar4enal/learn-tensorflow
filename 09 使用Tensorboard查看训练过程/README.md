��Python Shell��ִ�����´��룺

<pre>
import tensorflow as tf
import numpy as np

#��������
x_data = np.linspace(-1,1,300)[:, np.newaxis]
noise = np.random.normal(0,0.05, x_data.shape)
y_data = np.square(x_data)-0.5+noise

#�����
with tf.name_scope('input_layer'): #����㡣�������������ŵ�input_layer�������£�tensorboard������Ƿ���һ��ͼ������
����xs = tf.placeholder(tf.float32, [None, 1], name = 'x_input') # xs����x_input������ͼ������ʾ
����ys = tf.placeholder(tf.float32, [None, 1], name = 'y_input') # ys����y_input������ͼ������ʾ

#����
with tf.name_scope('hidden_layer'): #���㡣������Ȩ�ء�ƫ�á����������һ��
����with tf.name_scope('weight'): #Ȩ��
��������W1 = tf.Variable(tf.random_normal([1,10]))
��������tf.summary.histogram('hidden_layer/weight', W1)
����with tf.name_scope('bias'): #ƫ��
��������b1 = tf.Variable(tf.zeros([1,10])+0.1)
��������tf.summary.histogram('hidden_layer/bias', b1)
����with tf.name_scope('Wx_plus_b'): #������
��������Wx_plus_b1 = tf.matmul(xs,W1) + b1
��������tf.summary.histogram('hidden_layer/Wx_plus_b',Wx_plus_b1)
output1 = tf.nn.relu(Wx_plus_b1)

#�����
with tf.name_scope('output_layer'): #����㡣�������Ȩ�ء�ƫ�á����������һ��
����with tf.name_scope('weight'): #Ȩ��
��������W2 = tf.Variable(tf.random_normal([10,1]))
��������tf.summary.histogram('output_layer/weight', W2)
����with tf.name_scope('bias'): #ƫ��
��������b2 = tf.Variable(tf.zeros([1,1])+0.1)
��������tf.summary.histogram('output_layer/bias', b2)
����with tf.name_scope('Wx_plus_b'): #������
��������Wx_plus_b2 = tf.matmul(output1,W2) + b2
��������tf.summary.histogram('output_layer/Wx_plus_b',Wx_plus_b2)
output2 = Wx_plus_b2

#��ʧ
with tf.name_scope('loss'): #��ʧ
����loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-output2),reduction_indices=[1]))
����tf.summary.scalar('loss',loss)
with tf.name_scope('train'): #ѵ������
����train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#��ʼ��
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
merged = tf.summary.merge_all() #��ͼ�Ρ�ѵ�����̵����ݺϲ���һ��
writer = tf.summary.FileWriter('logs',sess.graph) #��ѵ����־д�뵽logs�ļ�����

#ѵ��
for i in range(1000):
����sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
����if(i%50==0): #ÿ50��дһ����־
��������result = sess.run(merged,feed_dict={xs:x_data,ys:y_data}) #������Ҫд�����־����
��������writer.add_summary(result,i) #����־����д���ļ�
</pre>

ִ���������룬���ڡ���ǰ·��/logs��Ŀ¼������һ��events.out.tfevents.{time}.{machine-name}���ļ����ڵ�ǰĿ¼�½����鿴ѵ������.bat�����������롣
 
<pre>
tensorboard --logdir=logs
</pre>

ִ������bat�ļ�����������������ַ��http://localhost:6006���Ϳ��Բ鿴ѵ�������еĸ���ͼ�Ρ�

**��Ҫ��ʾ���벻Ҫ����������Ŀ¼������Ŀ¼�п������κ�ͼ�Ρ����������������һ�ܣ�����**