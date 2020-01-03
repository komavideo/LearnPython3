# 导入模块
import func 

# print(func.add(10, 20))
# print(func.minus(10, 20))

# 导入模块并指定别名
import func as myfunc

# print(myfunc.add(100, 200))
# print(myfunc.minus(100, 200))

# 导入模块函数
from func import *
print(add(1000, 2000))
print(minus(1000, 2000))
