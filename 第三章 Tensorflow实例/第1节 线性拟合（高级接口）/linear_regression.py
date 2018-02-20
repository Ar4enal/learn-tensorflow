# 第1节 线性拟合（高级接口）

import tensorflow as tf
import numpy as np
import random

# 创建训练和测试数据集，y = x * 3 + 1 + noise
train_data = []
test_data = []
prediction_data = []

for i in range(100000):
  x = random.random()
  noise = random.random() * 0.0001
  y = x * 3 + 1 + noise
  train_data.append({ 'x': x, 'y': y })

for i in range(500):
  x = random.random()
  noise = random.random() * 0.0001
  y = x * 3 + 1 + noise
  test_data.append({ 'x': x, 'y': y })

for i in range(100):
  x = random.random()
  noise = random.random() * 0.0001
  y = x * 3 + 1 + noise
  prediction_data.append({ 'x': x, 'y': y })

train_x = [ i['x'] for i in train_data ]
train_y = [ i['y'] for i in train_data ]

test_x = [ i['x'] for i in test_data ]
test_y = [ i['y'] for i in test_data ]

prediction_x = { 'x': np.array([ i['x'] for i in  prediction_data]) }
prediction_y = [ i['y'] for i in prediction_data ]

# from_tensor_slices参数是一个元组，第一个元素是features，第二个元素是labels
train = tf.data.Dataset.from_tensor_slices(( { 'x': train_x }, train_y ))
test = tf.data.Dataset.from_tensor_slices(( { 'x': test_x }, test_y ))

# 创建线性回归模型
feature_columns = [
  tf.feature_column.numeric_column(key = 'x')
]
estimator = tf.estimator.LinearRegressor(feature_columns = feature_columns)

def input_train(): # 训练输入函数，打乱，然后取100个，可以循环取，生成一个迭代器
  return train.shuffle(1000).batch(100).repeat().make_one_shot_iterator().get_next()

def input_test(): # 评估输入函数
  return test.shuffle(1000).batch(100).make_one_shot_iterator().get_next()

def main(argv):
  # 使用数据训练模型，训练1000次
  estimator.train(input_fn = input_train, steps = 2000)

  # 评估模型
  eval_result = estimator.evaluate(input_fn = input_test)
  print(eval_result)

  # 使用模型进行预测
  predict_input_fn = tf.estimator.inputs.numpy_input_fn(prediction_x, shuffle = False)
  predict_results = estimator.predict(input_fn = predict_input_fn)
  for i, prediction in enumerate(predict_results):
    print('x=%s, y=%s, prediction=%s, error=%s'%(
      prediction_x['x'][i], 
      prediction_y[i], 
      prediction['predictions'][0], 
      str((prediction_y[i] - prediction['predictions'][0]) / prediction_y[i] * 100) + '%'
      ))

if __name__ == "__main__":
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run(main = main)