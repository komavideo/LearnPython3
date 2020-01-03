if条件式
========

## 知识点

* if逻辑条件判断

## 实战演习

~~~python
mylist = ["curry", "harden", "lebron", "durant", "kobe"]

for player in mylist:
    print(player)

# 等于
for player in mylist:
    if player == "lebron":
        print(player, "is king.")

# 不等于
for player in mylist:
    if player != "lebron":
        print(player, "is super star.")

# 列表存在判断
if "harden" in mylist:
    print("哈登在这儿。")

if "westbrook" not in mylist:
    print("神龟不在这儿。")

# 多个条件判断
pts_Russia = 0
pts_Uruguay = 0
if pts_Russia > 6 or pts_Uruguay > 6:
    print("俄罗斯或乌拉圭出线")

if pts_Russia > 6 and pts_Uruguay > 6:
    print("俄罗斯，乌拉圭携手出线")
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
