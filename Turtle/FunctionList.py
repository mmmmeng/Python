# coding=utf-8
# Author: mmmmeng

from prettytable import PrettyTable

# 声明列
columns = ["方法名", "参数列表", "说明"]

# 创建一张新表
table = PrettyTable(columns)

# 设置对齐方式
table.align[columns[0]] = "1"

# 设置填充宽度
table.padding_width = 5

# 添加行
table.add_row(["Turtle()", "none", "构造函数"])
table.add_row(["forward()", "像素值", "在当前方向移动像素值"])
table.add_row(["setpos()", "x,y ", "将光标移动到指定像素点"])
table.add_row(["up()", "none", "将光标抬起"])
table.add_row(["down()", "none", "将光标放下"])


# 输出表格
print(table)

















