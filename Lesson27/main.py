# 导入类
from mycore import Player, NbaPlayer

# 一次导入所有类
# from mycore import *

print("----------------------------------")
curry = Player("curry")
curry.sayHelo()
curry.intro()

print("----------------------------------")
curry = NbaPlayer("curry")
curry.sayHelo()
curry.intro()

# 系统模块导入
import sys
print("----------------------------------")
print(sys.version_info)
