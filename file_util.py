import csv
import os


def read_csv(filename):
    # 检查文件是否存在
    # 打开并读取CSV文件
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
