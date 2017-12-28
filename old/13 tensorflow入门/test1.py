# Getting Started With TensorFlow

import tensorflow as tf

# 常量
node1 = tf.constant(3.0, dtype = tf.float32)
node2 = tf.constant(4.0)

print(node1, node2)

# 会话
sess = tf.Session()
print(sess.run([node1, node2]))

# 运算
node3 = tf.add(node1, node2)
print('node3', node3)
print(sess.run(node3))

# 占位符
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b
print(sess.run(adder_node, { a: 3.0, b: 4.5 }))
print(sess.run(adder_node, { a: [1, 3], b: [2, 4] }))

# 乘法
add_and_triple = adder_node * 3
print('add_and_triple', sess.run(add_and_triple, { a: 3.0, b: 4.5 }))

# 变量
W = tf.Variable([.3], dtype = tf.float32)
b = tf.Variable([-.3], dtype = tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b

# 初始化
init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(linear_model, { x: [ 1, 2, 3, 4] }))

# 评估
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)

# 赋值
fixW = tf.assign(W, [-1. ])
fixb = tf.assign(b, [1. ])
sess.run([fixW, fixb])

print(sess.run(loss, { x: [ 1, 2, 3, 4 ], y: [ 0, -1, -2, -3 ] }))

# 训练
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

sess.run(init) # 将W和b的值恢复原状

for i in range(1000):
	sess.run(train, { x: [1, 2, 3, 4], y: [ 0, -1, -2, -3 ] })

print(sess.run([W, b]))

