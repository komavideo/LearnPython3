db_config = {
    "ip": "192.168.1.5",
    "port": 5432,
    "uid": "postgres",
    "pwd": "12345678"
}

# 遍历所有属性
# for key,val in db_config.items():
#     print(key, "=", val)
    # print(key, "\t=", val)

# 遍历所有key
# for key in db_config.keys():
#     print(key, " is ", db_config[key])

# 遍历所有的值
for val in db_config.values():
    print(val)
