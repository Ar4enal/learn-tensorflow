��python idle�����룺

<pre> 
import tensorflow as tf 

# ��������
hello = tf.constant('Hello,world!')

# �����Ự
sess = tf.Session()

# ִ��
result = sess.run(hello)

# �رջỰ
sess.close()

# ������
print</span>(result)
</pre>

</div>

�������к�����õ����b'Hello,world!'��֤�����гɹ���

ע�����

�� 1��Python3.0�Ժ�ʹ��print result�ᱨ����Ϊprint(result)���ɡ�