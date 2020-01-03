自建一个模块
===========

## 知识点

* 定义外部模块
* 引用外部模块

## 实战演习

### func.py

~~~python
def add(x, y):
    return x + y

def minus(x, y):
    return x - y
~~~

### main.py

~~~python
# 导入模块
import func 

print(func.add(10, 20))
print(func.minus(10, 20))

# 导入模块并指定别名
import func as myfunc

print(myfunc.add(10, 20))
print(myfunc.minus(10, 20))

# 导入模块函数
from func import *
print(add(10, 20))
print(minus(10, 20))
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
