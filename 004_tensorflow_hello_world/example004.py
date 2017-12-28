# 004 Tensorflow hello world

import tensorflow as tf 

# create a constant
hello = tf.constant('Hello,world!')

# create a session
sess = tf.Session()

# run to get the result
result = sess.run(hello)

# close session
sess.close()

# output the result
print(result)

# Run the code, and if you `b'Hello,world!'` in the console, 
# your have success in running your first tensorflow program.
