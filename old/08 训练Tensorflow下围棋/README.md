 这里介绍一下开源项目Mugo，它基于Tensorflow，可以使用sgf的棋谱训练围棋机器人，跟你下围棋，这里直接给出本人修改完善好的项目，只介绍一下用法。

 链接：[http://pan.baidu.com/s/1jHHA4D4](http://pan.baidu.com/s/1jHHA4D4) 密码：ksht

 准备工作：
 
 打开Windows PowShell，输入pip install argh，然后输入pip install sgf，将缺少的围棋python模块安装上。
 
 使用方法：
 
1. 将sgf的围棋棋谱放到data文件夹下面。（可以从https://u-go.net/gamerecords/下载）
2. 双击运行“z01 棋谱预处理.bat”，预处理棋谱。
3. 双击“z02 训练.bat”，使用棋谱训练模型。
4. 双击“z03 下棋.bat”，就可以跟训练出来的AI下棋。（也可以双击GoGui.exe，配置好机器人下棋，参数是python main.py gtp policy --read-file=tmp\savedmodel）

本人已经用棋谱训练了5万多次，围棋下的基本有那么那么点样了。

Github Mugo开源项目： [https://github.com/brilee/MuGo](https://github.com/brilee/MuGo)