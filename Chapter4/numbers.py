# range函数不包含最后一个参数的值
for value in range(1, 5):
    print(value)

message = list(range(1, 6))
print(message)

# 输出2-11（小于）中的数组，步长为2
step_number_list = list(range(2, 11, 2))
print(step_number_list)