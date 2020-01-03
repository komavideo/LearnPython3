myage = input("请输入你的年龄：")
print("你的年龄是：", myage)
print("-------------------")

# 年龄判断
# if int(myage) > 30:
#     print("现代老年人。")
# else:
#     print("加油啊，年轻人！")

# 数字判断
if myage.isnumeric():
    if int(myage) > 30:
        print("现代老年人。")
    else:
        print("加油啊，年轻人！")
else:
    print("火星年龄")