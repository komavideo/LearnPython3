# 返回数值
def add(x, y):
    return x + y
# print(add(10, 20))
# print(add(30, 50))

# 返回字符
# def makeDBString(ip, dbname, uid, pwd):
#     connString = ""
#     connString += "Server=" + ip + ";"
#     connString += "Database=" + dbname + ";"
#     connString += "Uid=" + uid + ";"
#     connString += "Pwd=" + pwd + ";"
#     return connString
# print(makeDBString("192.168.0.10", "myblog", "koma", "12345678"))

# 返回字典
def makeDBString(ip, dbname, uid, pwd):
    return {
        "Server": ip,
        "Database": dbname,
        "Uid": uid,
        "Pwd": pwd
    }

db = makeDBString("192.168.0.10", "myblog", "koma", "12345678")
print(db)
print(db["Server"])
print(db["Database"])
print(db["Uid"])
print(db["Pwd"])
