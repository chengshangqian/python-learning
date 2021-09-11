dimensions = (200, 50)
print(dimensions[0])
print(dimensions)
# 元组是元素不允许修改的列表,修改元组的元素将报错
# dimensions[0] = 400
for dimension in dimensions:
    print(dimension)

# 但可以该变元组本身
dimensions = (400, 500)
for dimension in dimensions:
    print(dimension)