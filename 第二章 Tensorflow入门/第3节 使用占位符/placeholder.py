# 第3节 使用占位符

# 占位符是一个可以在执行时赋值的容器。

import tensorflow as tf

# 创建一个占位符
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32, [2, 3]) # [2, 3]是形状，表示2*3的矩阵

sess = tf.Session()

result = sess.run([x, y], { x: 10, y: [[1, 2, 3], [4, 5, 6]] })

print('x=%s'%result[0])
print('y=%s'%result[1])

sess.close()