打开Python Shell，输入**import tensorflow as tf**，然后可以执行以下代码。

1、创建一个2*3的矩阵，并让所有元素的值为0.（类型为tf.float）

<pre>
a = tf.zeros([2,3], dtype = tf.float32)
</pre>

</div>

2、创建一个3*4的矩阵，并让所有元素的值为1.

<pre>
b = tf.ones([3,4])
</pre>

3、创建一个1*10的矩阵，使用2来填充。（类型为tf.int32，可忽略）

<pre>
c = tf.constant(2, dtype=tf.int32, shape=[1,10])
</pre>

4、创建一个1*10的矩阵，其中的元素符合正态分布，平均值是20，标准偏差是3.

<pre>
d = tf.random_normal([1,10],mean = 20, stddev = 3)
</pre>

上面所有的值都可以用来初始化变量。例如用0.01来填充一个1*2的矩阵来初始化一个叫bias的变量。

<pre>
bias = tf.Variable(tf.zeros([1,2]) + 0.01)
</pre>

如果你想查看这些量具体的值，可以在Session中执行它并输出。

<pre>
sess = tf.Session()
print(sess.run(d))
</pre>

这里，我得到了以下的值：

[[ 22.44503784, 18.19544983, 17.89671898, 17.67314911, 19.45074844,
18.6805439, 18.56541443, 16.59041977, 22.11240005, 19.12819099]]。它就是上面4我们创建的量的值。

参考资料

《Tensorflow学习笔记（3）》：[http://blog.sina.com.cn/s/blog_8b2a28790102wnkh.html](http://blog.sina.com.cn/s/blog_8b2a28790102wnkh.html)