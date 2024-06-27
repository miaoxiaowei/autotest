# 导入 xlrd 模块
import xlrd

# 把测试集中的NL2Code的生成结果，导出成独立java文件。
# 分为copilot/aixcoder/codegeex


def read_excel():
    # 读取 xls 文件的中作对象
    wb = xlrd.open_workbook(r"竞品分析结果.xls")
    # 定义生成的java类的名字【前缀+序号】
    copilot_template_name = "GenerateMethod"
    aix_template_name = "AIXGenerate"
    codegeex_template_name = "CGGenerate"

    file_prefix = ("package com.aixcode.autoTest.generate.{}; \n\nimport "
                   "com.aixcode.autoTest.GenerateMethodBase; \n\nimport java.util.List; \n\npublic class ")
    file_prefix2 = " extends GenerateMethodBase {\n"
    file_suffix = "\n}"
    # 获取所有的工作表名称
    sheet_names = wb.sheet_names()

    # 选择要读取的具体的工作表对象
    sheet = wb.sheet_by_name(sheet_names[0])

    # 查看工作表的行和列数
    if sheet.ncols < 7:
        print("invalid table contents~~")

    # 通过循环的方式获取工作表中的每行和每列的数据
    for row in range(1, sheet.nrows):
        # 通过cell对象中的value属性获取具体单元格的数据
        if len(str(sheet.cell(row, 0).value)) <= 0:
            continue

        test_id = int(sheet.cell(row, 0).value)
        aix_content = sheet.cell(row, 2).value
        copilot_content = sheet.cell(row, 4).value
        cg_content = sheet.cell(row, 6).value
        if copilot_content == "" or len(copilot_content) <= 0:
            continue
        else:
            creat_file(copilot_template_name + "{}.java".format(test_id),
                       file_prefix.format('copilot') + copilot_template_name + str(test_id) + file_prefix2 + copilot_content + file_suffix)
            creat_file(aix_template_name + "{}.java".format(test_id),
                       file_prefix.format('aixcoder') + aix_template_name + str(test_id) + file_prefix2 + aix_content + file_suffix)
            creat_file(codegeex_template_name + "{}.java".format(test_id),
                       file_prefix.format('codegeex') + codegeex_template_name + str(test_id) + file_prefix2 + cg_content + file_suffix)


def creat_file(file_name, file_contents):
    java_file = open(file_name, "w+")
    java_file.write(file_contents)
    java_file.close()


if __name__ == '__main__':
    read_excel()
