# 传递任意参数
def add(*num):
    result = 0
    for val in num:
        result += val
    return result

# result_sum = add(1,2,3)
# print(result_sum)

# result_sum = add(1,2,3,4,5,6,7,8,9,10)
# print(result_sum)


# 传递关键字参数
def sendmail(**data):
    for key, val in data.items():
        print(key, ":", val)

sendmail(
    subject="Python真不错",
    # content="我最近学习Python，感觉不错，赞一个！",
    to="test01@komavideo.com",
    # cc="xiaoma@komavideo.com",
    # try_times=5
)
