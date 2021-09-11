squares = []
for value in range(1, 6):
    squares.append(value**2)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

# 列表解析
new_squares = [value**2 for value in range(1, 6)]
print(new_squares)