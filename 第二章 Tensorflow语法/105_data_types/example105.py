# 105 Data types

import tensorflow as tf

# Tensorflow provide us with so many data types.
a = tf.constant(1, tf.float16)
b = tf.constant(2, tf.float32)
c = tf.constant(3, tf.float64)
#d = tf.constant(0b101001, tf.bfloat16)
e = tf.constant(5, tf.complex64)
f = tf.constant(6, tf.complex128)
g = tf.constant(7, tf.int8)
h = tf.constant(8, tf.int16)
i = tf.constant(9, tf.int32)
j = tf.constant(10, tf.int64)
k = tf.constant(True, tf.bool)
l = tf.constant('Hello,world!', tf.string)
#m = tf.constant(13, tf.qint8)
#n = tf.constant(14, tf.qint16)
#o = tf.constant(15, tf.qint32)
#p = tf.constant('~/1.txt', tf.resource)
#q = tf.constant(16, tf.variant)

