����ʹ��Tensorflow������((a+b)*c)^2/a��Ȼ����ƽ�����������룺

<pre>
import tensorflow as tf 

# ���봢������
a = tf.placeholder(tf.float16)
b = tf.placeholder(tf.float16)
c = tf.placeholder(tf.float16) 

# ����
d = tf.add(a, b) # �ӷ�
e = tf.multiply(d, c) # �˷�
f = tf.pow(e, 2) # ƽ��
g = tf.divide(f, a) #����
h = tf.sqrt(g) # ƽ����

# �Ự
sess = tf.Session()

# ��ֵ
feed_dict= { a:1, b:2, c:3 }

# ����
result = sess.run(h, feed_dict= feed_dict)

# �رջỰ
sess.close()

# ������
print(result)
</pre>

������a=1��b=2��c=3��������9.0��֤�����гɹ���

Tensorflow������ķ����ǣ��ȰѼ����ʽ�ӹ���һ��ͼ��Ȼ������ͼ�͸�ֵ��cpu��һ�����У������ٶȱȽϿ졣