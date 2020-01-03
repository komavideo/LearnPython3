json对象保存
============

## 知识点

* json对象写入
* json对象读出

## 实战演习

~~~python
import json

filename = "out/data.json"

mydata = {
    "title": "小马视频",
    "lessons": {
        "python": "制作中", 
        "vue": "完成", 
        "node": "完成"
    },
    "games": {
        "宝可梦探险寻宝": "奋斗中",
        "信长之野望": "通关",
        "GTA5": "打不下去了"
    },
}

# json对象写入
with open(filename, 'w', encoding='utf-8') as myfile:
    json.dump(mydata, myfile, indent=4)

# json对象读出
with open(filename, 'r', encoding='utf-8') as myfile:
    myjson = json.load(myfile)
    print(myjson)
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
