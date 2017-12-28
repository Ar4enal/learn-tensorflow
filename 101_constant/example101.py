# 101 Constant
import tensorflow as tf

a = tf.constant('Hello, world!')
b = tf.constant(1)
c = tf.constant(2.0)
d = tf.constant([1, 2])

# create a session
sess = tf.Session()

# run the result
result = sess.run([a, b, c, d])

print('a=%s'%result[0])
print('b=%s'%result[1])
print('c=%s'%result[2])
print('d=%s'%result[3])
print('done')

# close session
sess.close()
