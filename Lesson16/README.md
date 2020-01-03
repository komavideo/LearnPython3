遍历字典
========

## 知识点

* 遍历字典的元素
* 遍历字典的key
* 遍历字典的值

## 实战演习

~~~python
db_config = {
    "ip": "192.168.1.5",
    "port": 5432,
    "uid": "postgres",
    "pwd": "12345678"
}

# 遍历所有属性
for key,val in db_config.items():
    print(key, "=", val)
    # print(key, "\t=", val)

# 遍历所有key
for key in db_config.keys():
    print(key, " is ", db_config[key])

# 遍历所有的值
for val in db_config.values():
    print(val)
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
