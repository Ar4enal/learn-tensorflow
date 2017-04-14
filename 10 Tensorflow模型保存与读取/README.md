我们的模型训练出来想给别人用，或者是我今天训练不完，明天想接着训练，怎么办？这就需要模型的保存与读取。看代码：

<pre>
import tensorflow as tf
import numpy as np
import os

#输入数据
x_data = np.linspace(-1,1,300)[:, np.newaxis]
noise = np.random.normal(0,0.05, x_data.shape)
y_data = np.square(x_data)-0.5+noise

#输入层
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

#隐层
W1 = tf.Variable(tf.random_normal([1,10]))
b1 = tf.Variable(tf.zeros([1,10])+0.1)
Wx_plus_b1 = tf.matmul(xs,W1) + b1
output1 = tf.nn.relu(Wx_plus_b1)

#输出层
W2 = tf.Variable(tf.random_normal([10,1]))
b2 = tf.Variable(tf.zeros([1,1])+0.1)
Wx_plus_b2 = tf.matmul(output1,W2) + b2
output2 = Wx_plus_b2

#损失
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-output2),reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#模型保存加载工具
saver = tf.train.Saver()

#判断模型保存路径是否存在，不存在就创建
if not os.path.exists('tmp/'):
　　os.mkdir('tmp/')

#初始化
sess = tf.Session()
if os.path.exists('tmp/checkpoint'): #判断模型是否存在
　　saver.restore(sess, 'tmp/model.ckpt') #存在就从模型中恢复变量
else:
　　init = tf.global_variables_initializer() #不存在就初始化变量
　　sess.run(init)

#训练
for i in range(1000):
　　_,loss_value = sess.run([train_step,loss], feed_dict={xs:x_data,ys:y_data})
　　if(i%50==0): #每50次保存一次模型
　　　　save_path = saver.save(sess, 'tmp/model.ckpt') #保存模型到tmp/model.ckpt，注意一定要有一层文件夹，否则保存不成功！！！
　　　　print("模型保存：%s 当前训练损失：%s"%(save_path, loss_value))
</pre>

大家第一次训练得到：

模型保存：tmp/model.ckpt 当前训练损失：1.35421
模型保存：tmp/model.ckpt 当前训练损失：0.011808
模型保存：tmp/model.ckpt 当前训练损失：0.00916655
模型保存：tmp/model.ckpt 当前训练损失：0.00690887
模型保存：tmp/model.ckpt 当前训练损失：0.00575491
模型保存：tmp/model.ckpt 当前训练损失：0.00526401
模型保存：tmp/model.ckpt 当前训练损失：0.00498503
模型保存：tmp/model.ckpt 当前训练损失：0.00478226
模型保存：tmp/model.ckpt 当前训练损失：0.0046346
模型保存：tmp/model.ckpt 当前训练损失：0.00454276
模型保存：tmp/model.ckpt 当前训练损失：0.00446402
模型保存：tmp/model.ckpt 当前训练损失：0.00436883
模型保存：tmp/model.ckpt 当前训练损失：0.00427732
模型保存：tmp/model.ckpt 当前训练损失：0.00418589
模型保存：tmp/model.ckpt 当前训练损失：0.00409241
模型保存：tmp/model.ckpt 当前训练损失：0.00400956
模型保存：tmp/model.ckpt 当前训练损失：0.00392799
模型保存：tmp/model.ckpt 当前训练损失：0.00383506
模型保存：tmp/model.ckpt 当前训练损失：0.00373741
模型保存：tmp/model.ckpt 当前训练损失：0.00366922

第二次继续训练，得到：

模型保存：tmp/model.ckpt 当前训练损失：0.00412003
模型保存：tmp/model.ckpt 当前训练损失：0.00388735
模型保存：tmp/model.ckpt 当前训练损失：0.00382827
模型保存：tmp/model.ckpt 当前训练损失：0.00379988
模型保存：tmp/model.ckpt 当前训练损失：0.00378107
模型保存：tmp/model.ckpt 当前训练损失：0.003764
模型保存：tmp/model.ckpt 当前训练损失：0.00375149
模型保存：tmp/model.ckpt 当前训练损失：0.00374324
模型保存：tmp/model.ckpt 当前训练损失：0.00373386
模型保存：tmp/model.ckpt 当前训练损失：0.00372364
模型保存：tmp/model.ckpt 当前训练损失：0.00371543
模型保存：tmp/model.ckpt 当前训练损失：0.00370875
模型保存：tmp/model.ckpt 当前训练损失：0.00370262
模型保存：tmp/model.ckpt 当前训练损失：0.00369697
模型保存：tmp/model.ckpt 当前训练损失：0.00369161
模型保存：tmp/model.ckpt 当前训练损失：0.00368653
模型保存：tmp/model.ckpt 当前训练损失：0.00368169
模型保存：tmp/model.ckpt 当前训练损失：0.00367714
模型保存：tmp/model.ckpt 当前训练损失：0.00367274
模型保存：tmp/model.ckpt 当前训练损失：0.00366843

可以看到，第二次训练是在第一次训练的基础上继续训练的。于是，我们可以把我们想要的模型保存下来，慢慢训练。

参考文档：

1、《TensorFlow使用指南》：http://www.tensorfly.cn/tfdoc/tutorials/mnist_tf.html