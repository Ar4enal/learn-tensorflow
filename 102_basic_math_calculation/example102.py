# 102 Basic math calculation

import tensorflow as tf 

a = tf.add(1, 2) # a+b
b = tf.subtract(3, 1) # a-b
c = tf.multiply(2, 3) # a*b
d = tf.div(8, 4) # a/b
e = tf.pow(2, 3) # a^b
f = tf.sqrt(2.0) # sqrt(a)

# create a session
sess = tf.Session()

# calculate
result = sess.run([a, b, c, d, e, f])

# close session
sess.close()

# output the result
print('1+2=%s'%result[0])
print('3-1=%s'%result[1])
print('2*3=%s'%result[2])
print('8/4=%s'%result[3])
print('2^3=%s'%result[4])
print('sqrt(2.0)=%s'%result[5])
print('done')