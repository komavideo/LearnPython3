filename = "out/data.txt"

# 文件写入
with open(filename, 'w', encoding='utf-8') as myfile:
    myfile.write("你好，Python!\n")
    myfile.write("Helo Python!\n")
    myfile.write("Helo WorldCup 2018!\n")

# 文件读入
with open(filename, 'r', encoding='utf-8') as myfile:
    content = myfile.read()
    print(content)
