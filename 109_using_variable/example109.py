# 109 Using Variable

import tensorflow as tf

# create variables
a = tf.Variable(1)

sess = tf.Session()

sess.run(a.initializer)

for i in range(100):
	result = sess.run(a)
	print('i = %s'%i)

sess.close()