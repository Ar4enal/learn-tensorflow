打开Python Shell，先输入**import tensorflow as tf**，然后可以执行以下命令。

Tensorflow中的常量创建方法：

<pre>
hello = tf.constant('Hello,world!', dtype=tf.string)
</pre>

其中，'Hello,world!'是常量初始值；tf.string是常量类型，可以省略。常量和变量都可以去构建Tensorflow中的图。

Tensorflow中变量的创建方法：

<pre>
a = tf.Variable(10, dtype=tf.int32)
</pre>

其中，10是变量初始值，tf.int32是变量的类型。

Tensorflow中，主要有以下几种数据类型。

tf.int8：8位整数。

tf.int16：16位整数。

tf.int32：32位整数。

tf.int64：64位整数。

tf.uint8：8位无符号整数。

tf.uint16：16位无符号整数。

tf.float16：16位浮点数。

tf.float32：32位浮点数。

tf.float64：64位浮点数。

tf.double：等同于tf.float64。

tf.string：字符串。

tf.bool：布尔型。

tf.complex64：64位复数。

tf.complex128：128位复数。

参考资料：

《张量的阶、形状、数据类型》：[http://wiki.jikexueyuan.com/project/tensorflow-zh/resources/dims_types.html](http://wiki.jikexueyuan.com/project/tensorflow-zh/resources/dims_types.html)