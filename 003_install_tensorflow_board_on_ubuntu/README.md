# 003 Install tensorflow board on ubuntu

1. Open bash and type in `pip install tensorboard` or `pip3 install tensorboard`.

2. Open bash and type in `pip show tensorboard` to get the right install position.

For example, 

```bash
liteng@Lenovo-G470:~$ pip show tensorboard
Name: tensorboard
Version: 1.0.0a6
Summary: Standalone TensorBoard for visualizing in deep learning
Home-page: https://github.com/dmlc/tensorboard
Author: zihaolucky
Author-email: zihaolucky@gmail.com
License: Apache 2.0
Location: /home/liteng/.local/lib/python3.6/site-packages
Requires: werkzeug, Pillow, six, protobuf, numpy, wheel
```

. Your tensorboard is installed in `/home/liteng/.local/lib/python3.6/site-packages`.

2. Open bash and type in the code below, and your should get the right path of tensorboard.

```bash
python ~/.local/lib/python3.6/site-packages/tensorboard/main.py --logdir=logs
```

If you see

```
TensorBoard 0.4.0rc3 at http://Lenovo-G470:6006 (Press CTRL+C to quit)
```

, you have success in starting tensorboard. You can visit tensorboard at `http://localhost:6006` in you web brower.