# 第1节 线性拟合（自定义模型）

import tensorflow as tf
import numpy as np
import random

tf.logging.set_verbosity(tf.logging.INFO)

# 创建训练和测试数据集，y = x * 3 + 1 + noise
train_data = []

for i in range(100):
  x = random.random()
  noise = random.random() * 0.0001
  y = x * 3 + 1 + noise
  train_data.append({ 'x': x, 'y': y })

train_x = [ i['x'] for i in train_data ]
train_y = [ i['y'] for i in train_data ]

# 创建自定义模型
def model_fn(features, labels, mode):
  W = tf.get_variable('W', shape = [1], dtype = tf.float64)
  b = tf.get_variable('b', shape = [1], dtype = tf.float64)
  
  y = W * features['x'] + b

  loss = tf.reduce_sum(tf.square(y - labels))

  global_step = tf.train.get_global_step()
  optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)

  train = tf.group(
  	optimizer.minimize(loss),
  	tf.assign_add(global_step, 1)
  	)

  return tf.estimator.EstimatorSpec(
      mode = mode,
      predictions = y,
      loss = loss,
      train_op = train
      )

estimator = tf.estimator.Estimator(
	model_fn = model_fn,
	model_dir = 'tmp/model'
	)

# 开始训练
train_input_fn = tf.estimator.inputs.numpy_input_fn(
    { 'x': np.array(train_x) }, 
    np.array(train_y), 
    batch_size = 4, 
    num_epochs = None, 
    shuffle = True
    )

estimator.train(input_fn = train_input_fn, steps = 1000)