传递任意参数
===========

## 知识点

* 传递任意参数
* 传递关键字参数

## 实战演习

~~~python
# 传递任意参数
def add(*num):
    result = 0
    for val in num:
        result += val
    return result

result_sum = add(1,2,3)
print(result_sum)

result_sum = add(1,2,3,4,5)
print(result_sum)

# 传递关键字参数
def sendmail(**data):
    for key, val in data.items():
        print(key, ":", val)

sendmail(
    subject="Python真不错",
    content="我最近学习Python，感觉不错，赞一个！",
    to="test01@komavideo.com",
    cc="xiaoma@komavideo.com",
    try_times=5
)
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
