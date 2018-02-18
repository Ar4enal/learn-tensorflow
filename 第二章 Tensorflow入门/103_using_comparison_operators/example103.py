# 103 Using Comparison Operators

import tensorflow as tf

# constant
a = tf.constant(1)
b = tf.constant(2)

# comparison operators
c = tf.equal(a, b)
d = tf.not_equal(a, b)
e = tf.less(a, b)
f = tf.less_equal(a, a)
g = tf.greater(b, a)
h = tf.greater_equal(a, a)

# where operator
i = tf.where(tf.equal(a, a), 10, 11)
j = tf.where(tf.equal(a, b), 10, 11)

# create a session
sess = tf.Session()

# calculate the result
result = sess.run([c, d, e, f, g, h, i, j])

print('a equal b is %s'%result[0])
print('a not equal b is %s'%result[1])
print('a less than b is %s'%result[2])
print('a less equal than a is %s'%result[3])
print('b greater than a is %s'%result[4])
print('a greater equal than a is %s'%result[5])

print('a equal than a is true, so i=%s'%result[6])
print('a equal than b is false, so j=%s'%result[7])
