看代码：

<pre>
import tensorflow as tf
import numpy as np

# 构造输入数据（我们用神经网络拟合x_data和y_data之间的关系）
x_data = np.linspace(-1,1,300)[:, np.newaxis] # -1到1等分300份形成的二维矩阵
noise = np.random.normal(0,0.05, x_data.shape) # 噪音，形状同x_data在0-0.05符合正态分布的小数
y_data = np.square(x_data)-0.5+noise # x_data平方，减0.05，再加噪音值

# 输入层（1个神经元）
xs = tf.placeholder(tf.float32, [None, 1]) # 占位符，None表示n*1维矩阵，其中n不确定
ys = tf.placeholder(tf.float32, [None, 1]) # 占位符，None表示n*1维矩阵，其中n不确定

# 隐层（10个神经元）
W1 = tf.Variable(tf.random_normal([1,10])) # 权重，1*10的矩阵，并用符合正态分布的随机数填充
b1 = tf.Variable(tf.zeros([1,10])+0.1) # 偏置，1*10的矩阵，使用0.1填充
Wx_plus_b1 = tf.matmul(xs,W1) + b1 # 矩阵xs和W1相乘，然后加上偏置
output1 = tf.nn.relu(Wx_plus_b1) # 激活函数使用tf.nn.relu

# 输出层（1个神经元
W2 = tf.Variable(tf.random_normal([10,1]))
b2 = tf.Variable(tf.zeros([1,1])+0.1)
Wx_plus_b2</span> = tf.matmul(output1,W2) + b2
output2 = Wx_plus_b2

# 损失
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-output2),reduction_indices=[1])) # 在第一维上，偏差平方后求和，再求平均值，来计算损失
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss) # 使用梯度下降法，设置步长0.1，来最小化损失

# 初始化
init = tf.global_variables_initializer() # 初始化所有变量
sess = tf.Session()
sess.run(init) # 变量初始化

# 训练
for i in range(1000): #训练1000次
　_,loss_value = sess.run([train_step,loss],feed_dict={xs:x_data,ys:y_data}) # 进行梯度下降运算，并计算每一步的损失
　if(i%50==0):
　　print(loss_value) # 每50步输出一次损失
</pre>

</div>

输出：

0.405348
0.00954485
0.0068925
0.00551958
0.00471453
0.00425206
0.00400382
0.00381883
0.00367445
0.00353349
0.00341325
0.00330487
0.00321128
0.00313468
0.0030646
0.0030014
0.00294802
0.00290179
0.0028618
0.00282344

可以看到，随机训练的进行，损失越来越小，证明拟合越来越好。

参考资料：

《Tensorflow 自带可视化Tensorboard使用方法 附项目代码》：[http://blog.csdn.net/jerry81333/article/details/53004903](http://blog.csdn.net/jerry81333/article/details/53004903)

《tensorflow学习（六）：tensorflow中的tf.reduce_mean()这类函数》：[http://blog.csdn.net/qq_32166627/article/details/52734387](http://blog.csdn.net/qq_32166627/article/details/52734387)