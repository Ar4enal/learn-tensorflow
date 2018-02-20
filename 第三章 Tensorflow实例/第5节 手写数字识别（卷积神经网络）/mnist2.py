# 第4节 手写数字识别

import tensorflow as tf

# 获取数据集
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train.reshape([ -1, 28 * 28 ]) # shape (60000, 28, 28) => (60000, 28 * 28)
x_test = x_test.reshape([ -1, 28 * 28 ])

# 创建线性回归模型
feature_columns = [
  tf.feature_column.numeric_column(key = 'x')
]
estimator = tf.estimator.LinearRegressor(
  feature_columns = feature_columns,
  model_dir = 'tmp/model'
  )

def main(argv):
  # 训练
  train_input_fn = tf.estimator.inputs.numpy_input_fn(
  	x = { 'x': x_train },
  	y = y_train,
  	batch_size = 100,
  	num_epochs = None,
  	shuffle = True
  	)
  estimator.train(input_fn = train_input_fn, steps = 2000)

  # 评估
  eval_input_fn = tf.estimator.inputs.numpy_input_fn(
  	x = { 'x': x_test },
  	y = y_test,
  	batch_size = 100,
  	num_epochs = 1,
  	shuffle = False
  	)
  eval_result = estimator.evaluate(input_fn = eval_input_fn)
  print(eval_result)

if __name__ == "__main__":
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run(main = main)
