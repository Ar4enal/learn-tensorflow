��Python Shell������**import tensorflow as tf**��Ȼ�����ִ�����´��롣

1������һ��2*3�ľ��󣬲�������Ԫ�ص�ֵΪ0.������Ϊtf.float��

<pre>
a = tf.zeros([2,3], dtype = tf.float32)
</pre>

</div>

2������һ��3*4�ľ��󣬲�������Ԫ�ص�ֵΪ1.

<pre>
b = tf.ones([3,4])
</pre>

3������һ��1*10�ľ���ʹ��2����䡣������Ϊtf.int32���ɺ��ԣ�

<pre>
c = tf.constant(2, dtype=tf.int32, shape=[1,10])
</pre>

4������һ��1*10�ľ������е�Ԫ�ط�����̬�ֲ���ƽ��ֵ��20����׼ƫ����3.

<pre>
d = tf.random_normal([1,10],mean = 20, stddev = 3)
</pre>

�������е�ֵ������������ʼ��������������0.01�����һ��1*2�ľ�������ʼ��һ����bias�ı�����

<pre>
bias = tf.Variable(tf.zeros([1,2]) + 0.01)
</pre>

�������鿴��Щ�������ֵ��������Session��ִ�����������

<pre>
sess = tf.Session()
print(sess.run(d))
</pre>

����ҵõ������µ�ֵ��

[[ 22.44503784, 18.19544983, 17.89671898, 17.67314911, 19.45074844,
18.6805439, 18.56541443, 16.59041977, 22.11240005, 19.12819099]]������������4���Ǵ���������ֵ��

�ο�����

��Tensorflowѧϰ�ʼǣ�3������[http://blog.sina.com.cn/s/blog_8b2a28790102wnkh.html](http://blog.sina.com.cn/s/blog_8b2a28790102wnkh.html)