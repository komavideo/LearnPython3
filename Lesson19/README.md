while循环
==========

## 知识点

* while循环语法

## 实战演习

~~~python
# while的基本使用
i = 1
while i <= 8:
    print(i)
    i += 1

# break
result = 0
i = 1
while i <= 8:
    result += i
    i += 1
    if i > 5:
        break
print("result=", result)

# continue
i = 1
while i <= 8:
    if i % 2 == 1:
        i += 1
        continue
    print(i)
    i += 1
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
