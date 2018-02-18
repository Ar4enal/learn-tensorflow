# 第5节 条件运算

import tensorflow as tf

# 创建常量
a = tf.constant(1)
b = tf.constant(2)
c = tf.constant(3)

# 创建不同条件下执行的函数
def fun1():
	return a

def fun2():
	return b

def fun3():
	return c

# 如果a=b，则执行`fun1`；如果a不等于b，则执行fun2；否则执行fun3。并赋值给d
d = tf.case({ tf.equal(a, b): fun1, tf.not_equal(a, b): fun2 }, default=fun3)

sess = tf.Session()

result = sess.run(d)

print('d=%s'%result)
print('done')

sess.close()

# 由于a<b，则执行fun2，所以结果是d=2。