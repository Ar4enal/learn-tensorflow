# 第7节 循环语句

import tensorflow as tf

# 计算1加到100的值
i = tf.constant(0)
total = tf.constant(0)

def cond(i, total): # 条件
	return tf.less_equal(i, 100)

def body(i, total): # 循环体
	return [tf.add(i, 1), tf.add(total, i)] # i++, total += i

# 循环
loop = tf.while_loop(cond, body, [i, total]) # 第三个参数是传给`cond`和`body`的参数。

sess = tf.Session()

result = sess.run(loop)

print('i=%s, sum=%s'%(result[0], result[1]))

sess.close()