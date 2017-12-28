# 001 Install tensorflow on windows

1. Install python.

[Click here](https://www.python.org/downloads/release/python-352/) to download Python3.5.2, and install it.

2. Configure python environment.

add `%install_dir%\Scripts` to `Path`.

3. Change pip source.

If you are not in China, ignore this. In China, you can create a folder called `pip` in `C:\Users\{your username}\AppData\Local`, create a file called `pip.conf` with the content below.

```conf
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install] 
trusted-host=mirrors.aliyun.com  
```

4. Install tensorflow.

Open `PowerShell`, and execute the code below.

```bash
pip install --upgrade tensorflow
```

5. Test installation.

Open `Python IDLE`, type in `import tensorflow as tf`, and run. If there is no errors, congratulations! You have successfully install tensorflow.