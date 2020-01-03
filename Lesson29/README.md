错误处理
========

## 知识点

* try-except
* try-except-else
* try-except-else-finally

## 实战演习

~~~python
# 除0错误
print(10/0)

# 捕捉错误
try:
    print(10/0)
except ZeroDivisionError as zex:
    print("除0错误")
else:
    print("正常处理")
finally:
    print("End")
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
