导入外部类
==========

## 知识点

* 导入外部模块和外部类的方法

## 实战演习

### mycore.py

~~~python
class Player():
    def __init__(self, name):
        self.name = name

    def sayHelo(self):
        print("helo", self.name.title())

    def intro(self):
        print("I am player.")

class NbaPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.category = "nba"

    def intro(self):
        print("I am " + self.category + " player.")
~~~

### main.py

~~~python
# 导入类
# from mycore import Player, NbaPlayer

# 一次导入所有类
# from mycore import *

print("----------------------------------")
curry = Player("curry")
curry.sayHelo()
curry.intro()

print("----------------------------------")
curry = NbaPlayer("curry")
curry.sayHelo()
curry.intro()

# 系统模块导入
# import sys
# print(sys.version_info)
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
