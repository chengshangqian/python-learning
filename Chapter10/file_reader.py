# 一次读取
with open("D:\\temp\\data\\pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents)

# 逐行读取
filename = "pi_digits.txt"
with open(filename) as file_lines:
    for line in file_lines:
        # 去掉空白
        print(line.strip())

# 逐行读取
with open(filename) as file_list:
    lines = file_list.readlines()
    pi_value = ""
    for line in lines:
        pi_value += line.strip()
    print(pi_value)
    # 切片
    print(pi_value[:4])