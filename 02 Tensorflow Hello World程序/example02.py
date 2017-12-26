# 02 Tensorflow Hello World程序
import tensorflow as tf 

# 创建常量
hello = tf.constant('Hello,world!')

# 创建会话
sess = tf.Session()

# 执行
result = sess.run(hello)

# 关闭会话
sess.close()

# 输出结果
print(result)
