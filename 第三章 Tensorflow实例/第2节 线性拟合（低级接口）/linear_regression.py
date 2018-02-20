# 第1节 线性拟合（低级接口）

import tensorflow as tf
import random

# 创建训练和测试数据集，y = x * 3 + 1 + noise
train_data = []

for i in range(100):
  x = random.random()
  noise = random.random() * 0.0001
  y = x * 3 + 1 + noise
  train_data.append({ 'x': x, 'y': y })

train_x = [ i['x'] for i in train_data ]
train_y = [ i['y'] for i in train_data ]

# 创建线性回归模型
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

W = tf.Variable(tf.zeros([ len(train_data) ], dtype = tf.float32))
b = tf.Variable(tf.zeros([ len(train_data) ], dtype = tf.float32))

linear_model = W * x + b

loss = tf.sqrt(tf.reduce_sum(tf.square(linear_model - y)))

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

# 开始训练
sess = tf.Session()

saver = tf.train.Saver()

try:
  saver.restore(sess, save_path = 'tmp/model')
except:
  sess.run(init)

for i in range(200):
  _, error = sess.run((train, loss), { x: train_x, y: train_y })
  if i % 20 == 0:
    print('i=%s, loss=%s'%(i + 1, error))

saver.save(sess, save_path = 'tmp/model')

sess.close()