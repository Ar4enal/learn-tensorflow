# 第8节 产生随机数

import tensorflow as tf

a = tf.random_normal([1]) # 形状
b = tf.random_normal([2], 1.0, 0.5) # 形状，平均值
c = tf.random_normal([2, 3])

sess = tf.Session()

result = sess.run([a, b, c])

print('a=%s'%result[0])
print('b=%s'%result[1])
print('c=%s'%result[2])

sess.close()