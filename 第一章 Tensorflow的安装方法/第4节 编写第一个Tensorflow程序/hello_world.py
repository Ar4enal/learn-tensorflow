# 第4节 编写第一个Tensorflow程序

import tensorflow as tf

# 创建一个常量
hello = tf.constant('Hello, world!')

# 创建会话
sess = tf.Session()

# 执行程序并输出结果
result = sess.run(hello)
print(result)

# 关闭会话
sess.close()

# 执行这个python脚本，如果你看到`b'Hello,world!'`，你已经成功执行了第一个Tensorflow程序。