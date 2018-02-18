# 108 Circulation Operators

import tensorflow as tf

# Now let us calculate 1 to 100
i = tf.constant(0)
total = tf.constant(0)

cond = lambda i,total: tf.less_equal(i, 100)

body = lambda i, total: [tf.add(i, 1), tf.add(total, i)]


r = tf.while_loop(cond, body, [i, total])

sess = tf.Session()

result = sess.run(r)

print('i=%s,sum=%s'%(result[0], result[1]))

sess.close()