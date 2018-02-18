# 305 MNIST Softmax
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# From https://github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/examples/tutorials/mnist/mnist_softmax.py

# download data. Since we cannot visit google.com in China, so I change the source to lecun.com
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True, source_url="http://yann.lecun.com/exdb/mnist/")

# input data
x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])

# create model
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x, W) + b

# optimize
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# create session
sess = tf.Session()

# initialize the variables
init = tf.global_variables_initializer()
sess.run(init)

# start to train
for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# test the model
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

# The prediction should be about 91.7%