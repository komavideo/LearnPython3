变量与字符串
===========

## 知识点

* 变量的定义
* 字符串的基本使用

## 实战演习

### test.py

~~~python
# 数字变量
a = 1
b = 2
print(a+b)

# 字符变量
s1 = "helo"
s2 = "koma"
print(s1 + s2)
print(s1, s2)

# 字符函数
msg = "HELO world!"
print(msg)
print(msg.title())
print(msg.upper())
print(msg.lower())

# 转义字符
msg = "I can:\n\tPython\n\tJavascript"
print(msg)

# 删除余白
msg = " Curry is MVP. "
print("|" + msg + "|")
print("|" + msg.rstrip() + "|")
print("|" + msg.lstrip() + "|")
print("|" + msg.strip() + "|")
~~~

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
