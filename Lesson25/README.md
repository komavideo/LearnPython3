创建使用类
==========

## 知识点

* 定义和创建类
* 使用类方法和属性

## 实战演习

~~~python
class Player():
    def __init__(self, name):
        self.name = name

    def sayHelo(self):
        print("helo", self.name.title())

    def intro(self):
        print("I am player.")

curry = Player("curry")
print(curry.name)
curry.sayHelo()
curry.intro()

james = Player("james")
print(james.name)
james.sayHelo()
james.intro()
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
