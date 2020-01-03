# 除0错误
# print(10/0)

# 捕捉错误
try:
    print(10/10)
except ZeroDivisionError as zex:
    print("除0错误")
else:
    print("正常处理")
finally:
    print("End")
