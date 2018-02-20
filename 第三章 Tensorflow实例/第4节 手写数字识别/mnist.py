# 第4节 手写数字识别

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 模型
x = tf.placeholder(tf.float32, [None, 784]) # 28*28=784
y_ = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x, W) + b

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y_, logits = y))
train_step = tf.train.GradientDescentOptimizer(learning_rate = 0.5).minimize(cross_entropy)

init = tf.global_variables_initializer()

# 训练
sess = tf.Session()

sess.run(init)

for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict = {x: batch_xs, y_: batch_ys})

# 评估模型
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(sess.run(accuracy, feed_dict = {x: mnist.test.images, y_: mnist.test.labels}))

sess.close()
