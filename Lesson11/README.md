数组切片
========

## 知识点

* 使用数组切片来表示数组的一部分

## 实战演习

~~~python
fifa_ranking = []
fifa_ranking.append("Germany")
fifa_ranking.append("Brazil")
fifa_ranking.append("Belgium")
fifa_ranking.append("Portugal")
fifa_ranking.append("Argentina")
print(fifa_ranking)

# 切片定义
print(fifa_ranking[0:3])
print(fifa_ranking[1:4])
print(fifa_ranking[:3])
print(fifa_ranking[2:])

# 循环切片
for country in fifa_ranking[:3]:
    print(country)

# 复制切片
top3 = fifa_ranking[:3]
print(top3)

top3.append("Portugal")
print(top3)
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
