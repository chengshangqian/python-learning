import csv

filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 枚举列出第一行的每一列和索引位置
    for index, header_column in enumerate(header_row):
        print(index, header_column)
