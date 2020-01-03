文件的读写
==========

## 知识点

* 文件写入
* 文件读出

## 实战演习

~~~python
filename = "out/data.txt"

# 文件写入
with open(filename, 'w', encoding='utf-8') as myfile:
    myfile.write("你好，Python!\n")
    myfile.write("Helo Python!\n")

# 文件读出
with open(filename, 'r', encoding='utf-8') as myfile:
    content = myfile.read()
    print(content)
~~~

## API参考网站

https://docs.python.org/3/library/functions.html#open

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
