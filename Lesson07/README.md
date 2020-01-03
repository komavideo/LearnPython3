学学数组(列表)
=============

## 知识点

列表由一系列按特定顺序排列的元素组成。

* 数组的声明
* 数组的使用

## 实战演习

~~~python
# 数组的基本用法
mylist = ["curry", "harden", "lebron", "durant", "kobe"]
print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2].title())

# 修改元素
mylist[0] = "curry seth"
print(mylist[0])
print(mylist)

# 元素增加
mylist.append("antetokounmpo")
print(mylist)

lang_list = []
lang_list.append("Python")
lang_list.append("Javascript")
lang_list.append("Ruby on Rails")
lang_list.append("Swift/Kotlin")
lang_list.append("Java")
print(lang_list)

# 删除元素
del lang_list[0]
print(lang_list)
del lang_list[0]
print(lang_list)

deleted_item = lang_list.pop()
print(deleted_item)
print(lang_list)

# 指名删除
print(mylist)
mylist.remove("lebron")
print(mylist)
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
