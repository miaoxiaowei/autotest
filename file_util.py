import csv
import os


def read_csv(filename):
    # 检查文件是否存在
    if os.path.exists(filename):
        print(f"文件 {filename} 存在。下面是文件内容：")

        # 打开并读取CSV文件
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    else:
        print(f"文件 {filename} 不存在。")
