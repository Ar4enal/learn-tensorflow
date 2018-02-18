# 第1节 常量
import tensorflow as tf

a = tf.constant('Hello, world!')
b = tf.constant(1)
c = tf.constant(2.0, dtype = tf.float32)
d = tf.constant([1, 2])
e = tf.constant(5, dtype = tf.float32, shape = [2, 3])

# 创建一个会话
sess = tf.Session()

# 执行，并输出结果
result = sess.run([a, b, c, d, e])

print('a=%s'%result[0])
print('b=%s'%result[1])
print('c=%s'%result[2])
print('d=%s'%result[3])
print('e=%s'%result[4])
print('done')

# 关闭会话
sess.close()

# 说明：Tensorflow支持的数据类型很多，例如：
# a = tf.constant(1, tf.float16)
# b = tf.constant(2, tf.float32)
# c = tf.constant(3, tf.float64)
# e = tf.constant(5, tf.complex64)
# f = tf.constant(6, tf.complex128)
# g = tf.constant(7, tf.int8)
# h = tf.constant(8, tf.int16)
# i = tf.constant(9, tf.int32)
# j = tf.constant(10, tf.int64)
# k = tf.constant(True, tf.bool)
# l = tf.constant('Hello,world!', tf.string)