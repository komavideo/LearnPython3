db_config = {
    "ip": "192.168.1.5",
    "port": 5432,
    "uid": "postgres",
    "pwd": "12345678",
    "options": {
        "timeout": 300,
        "encode": "utf-8"
    },
    "drivers": ["pgsql", "Npgsql", "jdbpgsql"]
}

# print(db_config)
# print(db_config["options"])
# print(db_config["drivers"])

# options = db_config["options"]
# for key,val in options.items():
#     print(key, "=", val)

drivers = db_config["drivers"]
for val in drivers:
    print(val)
