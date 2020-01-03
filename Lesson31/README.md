turtle - 内置的海龟绘图库
=================

## 知识点

+ 学会使用Python的绘图库
+ 画出我们自己图像

## 官网

https://docs.python.org/zh-cn/3/library/turtle.html

## 安装确认

```bash
$ python -m turtle
```

### 缺少python-tk的问题

```bash
$ sudo apt-get install python-tk
```

## 实战

### 基本操作

+ color:设置颜色
+ shape:设置光标形状
+ forward:前进
+ backward:后退
+ left:左转
+ right:右转
+ circle:画圆
+ speed:设置绘图速度
+ reset:重置初始状态
+ up:画笔抬起
+ down:画笔落下
+ goto:移动光标位置
+ etc.

### 代码

```python
from turtle import *

# color("green")
# shape("turtle")

speed(1) # 慢
# speed(10) # 最快
# speed(0) # 极速(取消动画效果)

forward(100)
# backward(30)
# circle(100)

# def drawIt():
#     forward(100)
#     left(90)

# for i in range(4):
#     drawIt()

# color('red')
# circle(100)

# def star(size):
#     for i in range(5):
#         forward(size)
#         right(180 - 180/5)

# star(50)
# color('red')
# begin_fill()
# star(50)
# end_fill()

# up()
# goto(100,100)
# down()
# star(50)

done()
```

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
