打开python idle，输入：

<pre> 
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
print</span>(result)
</pre>

</div>

　　运行后，如果得到输出b'Hello,world!'，证明运行成功。

注意事项：

　 1、Python3.0以后，使用print result会报错，改为print(result)即可。