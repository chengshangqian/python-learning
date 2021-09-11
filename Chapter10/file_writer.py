filename = "programming.txt"
with open(filename, "w") as file_writer:
    file_writer.write("I love programming.")
    # append
    file_writer.write("I love programming.")
    # 换行
    file_writer.write("I love programming.\n")
    file_writer.write("I love programming.")
    # 数字需要使用str格式化为字符串后才能存储
    file_writer.write(str(123))

with open(filename) as file_reader:
    # 读取出来的都是字符串，注意，数字需要使用int或float方法转换才能使用
    print(file_reader.read())

with open(filename, "a") as file_appender:
    # 在原来文件上添加内容
    file_appender.write("I love programming---.")
    file_appender.write("I love programming---.")

with open(filename) as file_reader:
    print(file_reader.read())