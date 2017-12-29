# 104 Using Conditional Operators

import tensorflow as tf

# constant
a = tf.constant(1)
b = tf.constant(2)
c = tf.constant(3)

# using conditonal operators
f1 = lambda: a
f2 = lambda: b
f3 = lambda: c

d = tf.case({ tf.equal(a, b): f1, tf.not_equal(a, b): f2 }, default=f3)

sess = tf.Session()

result = sess.run(d)

print('c=%s'%result)
print('done')

sess.close()

## As we all know, a equals b is wrong, and a not euqals b is right. So the result should be `c=2`.