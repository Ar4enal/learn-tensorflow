import tensorflow as tf 

# 输入储存容器
a = tf.placeholder(tf.float16)
b = tf.placeholder(tf.float16)
c = tf.placeholder(tf.float16) 

# 计算
d = tf.add(a, b) # 加法
e = tf.multiply(d, c) # 乘法
f = tf.pow(e, 2) # 平方
g = tf.divide(f, a) #除法
h = tf.sqrt(g) # 平方根

# 会话
sess = tf.Session()

# 赋值
feed_dict= { a:1, b:2, c:3 }

# 计算
result = sess.run(h, feed_dict= feed_dict)

# 关闭会话
sess.close()

# 输出结果
print(result)
