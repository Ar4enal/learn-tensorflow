# 第9节 字符串操作

import tensorflow as tf

a = tf.constant('Hello,world!')
b = tf.constant('I love tensorflow.')

sess = tf.Session()

# 计算哈希值
c = tf.string_to_hash_bucket_fast(a, 10000000)
d = tf.string_to_hash_bucket_strong(a, 10000000, key = [1,3])
e = tf.string_to_hash_bucket(a, 10000000)
result = sess.run([c, d, e])

print('Hashing:\nfast:%s\nstrong:%s\nnormal:%s\n\n'%(result[0], result[1], result[2]))

# 把数组连接为字符串
c = tf.reduce_join([a, b], axis=0)
d = tf.string_join([a, b], '__')

result = sess.run([c, d])

print('Joining:\nc=%s\nd=%s\n\n'%(result[0], result[1]))

# 分割字符串
c = tf.string_split([a], ',')
d = tf.substr(a, 0, 5)

result = sess.run([c, d])

print('Spliting:\nc=%s\nd=%s\n\n'%(result[0][1],result[1]))

# 转换字符串
c = tf.as_string(tf.constant(10))
d = tf.string_to_number(c)
e = tf.encode_base64(a)
f = tf.decode_base64(e)

result = sess.run([c, d, e, f])

print('Conversion:\nc=%s\nd=%s\ne=%s\nf=%s\n\n'%(result[0], result[1], result[2], result[3]))

sess.close()