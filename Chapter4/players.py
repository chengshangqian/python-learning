# 对列表切片
players = ['Qian', 'jie', 'feng', 'quan', 'liang']

# 前面3个（指定开始和结束索引的元素）
print(players[0:3])
print(players[2:4])

# 不指定开始元素索引，默认从第一个元素开始
print(players[:2])

# 不指定结束索引，默认到最后一个元素结束
print(players[3:])

# 切取最后N个元素: 切取最后3个元素
print(players[-3:])

# 切取倒数第3个元素
print(players[-3])

# 切取倒数第N个元素之前的所有元素
print(players[:-3])

# 遍历切片
for player in players[:4]:
    print(player)