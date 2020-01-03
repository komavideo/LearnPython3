# i = 1
# while i <= 8:
#     print(i)
#     i += 1

# break
# result = 0
# i = 1
# while i <= 8:
#     result += i
#     print(result)
#     i += 1
#     if i > 5:
#         break
# print("result=", result)

# continue
i = 1
while i <= 8:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1