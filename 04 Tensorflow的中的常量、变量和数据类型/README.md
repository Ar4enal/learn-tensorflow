��Python Shell��������**import tensorflow as tf**��Ȼ�����ִ���������

Tensorflow�еĳ�������������

<pre>
hello = tf.constant('Hello,world!', dtype=tf.string)
</pre>

���У�'Hello,world!'�ǳ�����ʼֵ��tf.string�ǳ������ͣ�����ʡ�ԡ������ͱ���������ȥ����Tensorflow�е�ͼ��

Tensorflow�б����Ĵ���������

<pre>
a = tf.Variable(10, dtype=tf.int32)
</pre>

���У�10�Ǳ�����ʼֵ��tf.int32�Ǳ��������͡�

Tensorflow�У���Ҫ�����¼����������͡�

tf.int8��8λ������

tf.int16��16λ������

tf.int32��32λ������

tf.int64��64λ������

tf.uint8��8λ�޷���������

tf.uint16��16λ�޷���������

tf.float16��16λ��������

tf.float32��32λ��������

tf.float64��64λ��������

tf.double����ͬ��tf.float64��

tf.string���ַ�����

tf.bool�������͡�

tf.complex64��64λ������

tf.complex128��128λ������

�ο����ϣ�

�������Ľס���״���������͡���[http://wiki.jikexueyuan.com/project/tensorflow-zh/resources/dims_types.html](http://wiki.jikexueyuan.com/project/tensorflow-zh/resources/dims_types.html)