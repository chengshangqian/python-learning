import csv

"""终端指安装源安装模块：pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple """
from matplotlib import pyplot as plt

from datetime import datetime

filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)

    # 读取第一行
    header_row = next(reader)
    # 枚举列出第一行的每一列和索引位置
    for index, header_column in enumerate(header_row):
        print(index, header_column)

    # 读取接下来的数据行中的第2列
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        # 转为数字
        high = int(row[1])
        highs.append(high)

    print(highs)

    # 使用matplotlib模块绘制图形展示每日高温
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c="red")
    plt.title("Daily High Temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.show()
