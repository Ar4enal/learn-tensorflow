# 第4节 手写数字识别

import tensorflow as tf

# 获取数据集
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train.astype('float32')
y_train = y_train.astype('int32')

x_test = x_test.astype('float32')
y_test = y_test.astype('int32')

# 模型
def cnn_model_fn(features, labels, mode):
  input_layer = tf.reshape(features['x'], [-1, 28, 28, 1])

  # 第一层卷积
  conv1 = tf.layers.conv2d(
    inputs = input_layer,
    filters = 32,
    kernel_size = [5, 5],
    padding = 'same',
    activation = tf.nn.relu
    )
  pool1 = tf.layers.max_pooling2d(
    inputs = conv1,
    pool_size = [2, 2],
    strides = 2
    )

  # 第二层卷积
  conv2 = tf.layers.conv2d(
    inputs = pool1,
    filters = 64,
    kernel_size = [5, 5],
    padding = 'same',
    activation = tf.nn.relu
    )
  pool2 = tf.layers.max_pooling2d(
    inputs = conv2,
    pool_size = [2, 2],
    strides = 2
    )
  pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])

  # dense层
  dense = tf.layers.dense(
    inputs = pool2_flat,
    units = 1024,
    activation = tf.nn.relu
    )
  dropout = tf.layers.dropout(
    inputs = dense,
    rate = 0.4,
    training = mode == tf.estimator.ModeKeys.TRAIN
    )
  logits = tf.layers.dense(
    inputs = dropout,
    units = 10
    )
  loss = tf.losses.sparse_softmax_cross_entropy(labels = labels, logits = logits)

  # 训练函数
  def train_fn():
    optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.001)
    train_op = optimizer.minimize(
      loss = loss,
      global_step = tf.train.get_global_step()
      )
    return tf.estimator.EstimatorSpec(
      mode = mode,
      loss = loss,
      train_op = train_op
      )

  # 评估函数
  def eval_fn():
    eval_metric_ops = {
    'accuracy': tf.metrics.accuracy(
      labels = labels,
      predictions = tf.argmax(input = logits, axis = 1)
      )
    }
    return tf.estimator.EstimatorSpec(
      mode = mode,
      loss = loss,
      eval_metric_ops = eval_metric_ops
      )

  # 预测函数
  def predict_fn():
    return tf.estimator.EstimatorSpec(
      mode = mode, 
      predictions = {
      'classes': tf.argmax(input = logits, axis = 1),
      'probabilities': tf.nn.softmax(logits, name = 'softmax_tensor')
      }
      )

  if mode == tf.estimator.ModeKeys.TRAIN:
    return train_fn()
  elif mode == tf.estimator.ModeKeys.EVAL:
    return eval_fn()
  else: # tf.estimator.ModeKeys.PREDICT
    return predict_fn()

def main(argv):
  estimator = tf.estimator.Estimator(
    model_fn = cnn_model_fn,
    model_dir = 'tmp/model'
    )

  # 训练
  train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x = { 'x': x_train },
    y = y_train,
    batch_size = 100,
    num_epochs = None,
    shuffle = True
    )
  estimator.train(
    input_fn = train_input_fn,
    steps = 1000
    )

  # 评估
  eval_input_fn = tf.estimator.inputs.numpy_input_fn(
    x = { 'x': x_test },
    y = y_test,
    num_epochs = 1,
    shuffle = False
    )
  eval_results = estimator.evaluate(input_fn = eval_input_fn)
  print(eval_results)

if __name__ == "__main__":
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run(main = main)