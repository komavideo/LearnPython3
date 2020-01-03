元组的使用
==========

元组是一种特殊的数组(列表)，是一种不可变的数组 。

## 知识点

* 通过小括号()定义元组
* 元组是不可变的数组(列表)

## 实战演习

~~~python
tuple_sample = (1, 2, 3, 5, 8, 13)

print(tuple_sample)
print(tuple_sample[0])
print(tuple_sample[1])
print(tuple_sample[2])

# 循环元组
for val in tuple_sample:
    print(val)

# 元组不变值
# tuple_sample[0] = 10

# 元组重新设置
tuple_sample = ("a", "b", "c")
print(tuple_sample)
for val in tuple_sample:
    print(val)
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
