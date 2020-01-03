fifa_ranking = []
fifa_ranking.append("Germany")
fifa_ranking.append("Brazil")
fifa_ranking.append("Belgium")
fifa_ranking.append("Portugal")
fifa_ranking.append("Argentina")
print(fifa_ranking)

# 切片定义
# print(fifa_ranking[0:3])
# print(fifa_ranking[1:4])
# print(fifa_ranking[:3])
# print(fifa_ranking[2:])

# 循环切片
# for country in fifa_ranking[:3]:
#     print(country)

# 复制切片
top3 = fifa_ranking[:3]
print(top3)

top3.append("Portugal")
print(top3)