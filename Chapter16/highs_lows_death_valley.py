import csv

"""终端指安装源安装模块：pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple """
from matplotlib import pyplot as plt

from datetime import datetime

filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    # 读取第一行
    header_row = next(reader)
    # 读取接下来的数据行中的第2列
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "Missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # 使用matplotlib模块绘制图形展示每日高低温
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c="red", alpha=0.5)
    plt.plot(dates, lows, c="blue", alpha=0.5)
    # 着色
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
    title = "Daily High And Low Temperatures - 2014\nDeath Valley, CA"
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.show()
