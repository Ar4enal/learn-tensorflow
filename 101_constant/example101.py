# 101 Constant
import tensorflow as tf

a = tf.constant('Hello, world!')
b = tf.constant(1)
c = tf.constant(2.0, dtype = tf.float32)
d = tf.constant([1, 2])
e = tf.constant(5, dtype = tf.float32, shape = [2, 3])

# create a session
sess = tf.Session()

# run the result
result = sess.run([a, b, c, d, e])

print('a=%s'%result[0])
print('b=%s'%result[1])
print('c=%s'%result[2])
print('d=%s'%result[3])
print('e=%s'%result[4])
print('done')

# close session
sess.close()
