lambda - 匿名函数的基本用法
===================

## 知识点

+ lambda式的基本使用方法

## 实战演习

### 定义匿名函数

```python
def add(a, b=1):
    return a + b
print(add(10,20))
print(add(10))

add_lambda = lambda a, b=1: a + b
print(add_lambda(10,20))
print(add_lambda(10))
```

### 使用if条件文

```python
# 利用三项表达式
get_odd_even = lambda x: 'even' if x % 2 == 0 else 'odd'

print(get_odd_even(8))
print(get_odd_even(9))
```

### 无参数表达式

```python
import random

ran_lambda = lambda: random.random()

print(ran_lambda())
print(ran_lambda())
print(ran_lambda())
```

### 活用例：map()

```python
def add(x):
    return x ** 2

mobj = map(add, [1,2,3,4])
print(list(mobj))

mobj = map(lambda x:x**2, [1,2,3,4])
print(list(mobj))
```

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com