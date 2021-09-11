import json
import pygal

filename = "btc_close_2017.json"
dates, months, weeks, weekdays, closes = [], [], [], [], []
with open(filename, "r") as f:
    contents = json.load(f)
    for content in contents:
        date = content["date"]
        dates.append(date)
        month = int(content["month"])
        months.append(month)
        week = int(content["week"])
        weeks.append(week)
        weekday = content["weekday"]
        weekdays.append(weekday)
        close = int(float(content["close"]))
        closes.append(close)
        # print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = "收盘价(￥)"
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
line_chart.add("收盘价", closes)
line_chart.render_to_file("收盘价折线图(￥).svg")