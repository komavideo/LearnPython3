# def add(x):
#     return x ** 2

# mobj = map(add, [1,2,3,4])
# print(list(mobj))

mobj = map(lambda x:x**2, [1,2,3,4,5])
print(list(mobj))
