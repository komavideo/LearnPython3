类继承
======

## 知识点

* 类继承的知识

## 实战演习

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
        print("I am a " + self.category + " player.")

print("----------------------------------")
curry = Player("curry")
curry.sayHelo()
curry.intro()

print("----------------------------------")
curry = NbaPlayer("curry")
curry.sayHelo()
curry.intro()
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
