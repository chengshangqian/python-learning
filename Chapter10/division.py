try:
    result = 5 / 1
except ZeroDivisionError as zdError:
    print("You can't division by zero:" + str(zdError))
    result = 0
else:
    """如果没有抛出异常"""
    result *= 2

# 没有异常继续往下运行
print("result = " + str(result))
