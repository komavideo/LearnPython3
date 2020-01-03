mylist = ["curry", "harden", "lebron", "durant", "kobe"]

# for player in mylist:
#     print(player)

# 等于
# for player in mylist:
#     if player == "lebron":
#         print(player, "is king.")

# 不等于
# for player in mylist:
#     if player != "lebron":
#         print(player, "is super star.")

# 列表存在判断
# if "harden" in mylist:
#     print("哈登在这儿。")

# if "westbrook" not in mylist:
#     print("神龟不在这儿。")

# 多个条件判断
pts_Russia = 7
pts_Uruguay = 7
if pts_Russia > 6 or pts_Uruguay > 6:
    print("俄罗斯或乌拉圭出线")

if pts_Russia > 6 and pts_Uruguay > 6:
    print("俄罗斯，乌拉圭携手出线")
