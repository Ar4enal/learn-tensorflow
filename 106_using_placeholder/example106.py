# 106 Using placeholder

# Placeholder is something that you can feed data later.

import tensorflow as tf

# create a placeholder
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32, [2, 3])

sess = tf.Session()

result = sess.run([x, y], { x: 10, y: [[1, 2, 3], [4, 5, 6]] })

print('x=%s'%result[0])
print('y=%s'%result[1])

sess.close()