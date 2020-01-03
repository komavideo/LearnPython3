db_config = {
    "ip": "192.168.1.5",
    "port": 5432,
    "uid": "postgres",
    "pwd": "12345678"
}

print(db_config)
# print(db_config["ip"])
# print(db_config["port"])
# print(db_config["uid"])
# print(db_config["pwd"])

# 新增一个属性
db_config["timeout"] = 300
print("\n")
print(db_config)
# print(db_config["timeout"])

# # 修改属性值
# db_config["timeout"] = 60
# print(db_config)
# print(db_config["timeout"])

# 删除属性
del db_config["timeout"]
print("\n")
print(db_config)
# print(db_config["timeout"])