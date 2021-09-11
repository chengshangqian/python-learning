bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())

# 访问列表最后一个元素
print(bicycles[-1])

# 修改列表的元素
bicycles[-1] = 'last_one'
print(bicycles[-1])
print(bicycles)

# 在列表末尾加入元素
bicycles.append("new_one")
print(len(bicycles))
print(bicycles[-1])

bicycles.insert(0, 'first_one')
print(bicycles)

# 删除列表中最后一元素
del bicycles[-1]
print(bicycles)
# 弹出/删除最后一个元素
elem = bicycles.pop()
print(elem)
print(bicycles)
# 弹出第一个元素
first_one = bicycles.pop(0)
print(first_one)
print(bicycles)
# 根据值删除【第一个匹配】的元素
bicycles.remove('trek')
print(bicycles)

print(sorted(bicycles))
print(bicycles)

bicycles.reverse()
print(bicycles)

bicycles.sort()
print(bicycles)

bicycles.sort(reverse=True)
print(bicycles)
