# 使用range()函数
# for val in range(5):
#     print(val)
# for(int i = 0; i < 5; i++) {
# }

# 指定range()的范围
# for val in range(1, 5):
#     print(val)
# for(int i = 1; i < 5; i++) {
# }

# 生成数组
# nums = list(range(1,5))
# print(range(1,5))
# print(nums)

# 奇数数组
# nums = list(range(1,11,2))
# print(nums)

# 偶数数组
# nums = list(range(0,11,2))
# print(nums)

# 处理函数
# nums = [1,3,5,7,9,2,4,6,8,10]
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# lambda写法
nums = [val*2 for val in range(1,5)]
print(nums)

nums = []
for val in range(1,5):
    nums.append(val*2)
print(nums)
