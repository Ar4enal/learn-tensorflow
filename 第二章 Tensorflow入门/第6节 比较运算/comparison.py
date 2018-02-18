# 第6节 比较运算

import tensorflow as tf

# 常量
a = tf.constant(1)
b = tf.constant(2)

# 各种比较运算符
c = tf.equal(a, b)
d = tf.not_equal(a, b)
e = tf.less(a, b)
f = tf.less_equal(a, a)
g = tf.greater(b, a)
h = tf.greater_equal(a, a)

# where运算，如果条件成立，返回第二个参数，不成立，返回第三个参数
i = tf.where(tf.equal(a, a), 10, 11)
j = tf.where(tf.equal(a, b), 10, 11)

sess = tf.Session()
result = sess.run([c, d, e, f, g, h, i, j])

print('a equal b is %s'%result[0])
print('a not equal b is %s'%result[1])
print('a less than b is %s'%result[2])
print('a less equal than a is %s'%result[3])
print('b greater than a is %s'%result[4])
print('a greater equal than a is %s'%result[5])

print('a equal than a is true, so i=%s'%result[6])
print('a equal than b is false, so j=%s'%result[7])
