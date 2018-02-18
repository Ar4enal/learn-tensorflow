# 第4节 使用变量

import tensorflow as tf

# 创建变量
x = tf.Variable(0) # 初始值为0

sess = tf.Session()

# 初始化变量（变量使用前必须初始化或赋值）
sess.run(x.initializer) # 或者使用`tf.global_variables_initializer()`初始化所有变量

for i in range(100):
	update = tf.assign_add(x, i + 1)
	sess.run(update)

# 输出1加到100的结果
result = sess.run(x)
print('result = %s'%result)

sess.close()