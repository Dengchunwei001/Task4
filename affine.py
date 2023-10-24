import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math
import tkinter as tk
import sys
from tkinter import colorchooser
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter import colorchooser
from collections import namedtuple
import numpy as np

flagDot = False  # 标志位：是否在点击后绘制点
flagSegment = False  # 标志位：是否在点击后绘制线段
flagPolygon = False  # 标志位：是否在点击后绘制多边形
flagMakePolygon = False  # 标志位：是否在点击后制作多边形
flagPolygonExist = False  # 标志位：是否已经存在多边形
FlagClicMove = False  # 标志位：是否在点击后进行移动操作
points = []  # 存储绘制的点或多边形的顶点坐标


# 定义画布上的点击事件处理函数
# 定义画布上的点击事件处理函数
def draw(event):
    global points, flagDot, flagSegment, flagPolygon, flagMakePolygon, canvas, dx, dy

    if flagDot:
        # 如果 flagDot 为 True，则执行以下操作
        # 这表示用户希望绘制一个点
        dx, dy = event.x, event.y  # 记录鼠标点击的坐标
        x, y = event.x, event.y
        # 在画布上创建一个小椭圆代表一个点
        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", outline='white')
        flagDot = False  # 将 flagDot 设置为 False，取消绘制点

    if flagSegment:
        # 如果 flagSegment 为 True，则执行以下操作
        # 这表示用户希望绘制线段
        x, y = event.x, event.y  # 获取鼠标点击的坐标
        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", outline='white')
        # 在画布上创建一个小椭圆代表一个点
        points.append((x, y))  # 将点的坐标添加到列表 points 中
        if len(points) == 2:
            # 如果已经收集了两个点的坐标
            draw_segment()  # 调用函数绘制线段
            points.clear()  # 清空点的坐标列表
            flagSegment = False  # 将 flagSegment 设置为 False，取消绘制线段

    if flagPolygon:
        # 如果 flagPolygon 为 True，则执行以下操作
        # 这表示用户希望绘制多边形
        x, y = event.x, event.y  # 获取鼠标点击的坐标
        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", outline='white')
        # 在画布上创建一个小椭圆代表一个点
        points.append([x, y])  # 将点的坐标添加到列表 points 中


# 定义绘制点的按钮点击事件处理函数
def fDot():
    global flagDot
    # 声明一个全局变量 flagDot，用于标识是否在点击后绘制点

    flagDot = True
    # 当用户点击 "fDot" 按钮时，将 flagDot 设置为 True
    # 这表示用户希望绘制一个点


# 定义绘制线段的按钮点击事件处理函数
def fSegment():
    global flagSegment
    flagSegment = True


# 定义绘制多边形的按钮点击事件处理函数
def fPolygon():
    global flagPolygon, points
    points.clear()
    flagPolygon = True


# 定义绘制多边形按钮的点击事件处理函数
def fMakePolygon():
    global flagMakePolygon
    flagMakePolygon = True


# 绘制线段
# 定义绘制线段的函数
def draw_segment():
    global points, canvas
    # 声明使用全局变量 points 和 canvas

    dot1 = points[0]
    dot2 = points[1]
    # 从 points 列表中获取前两个点的坐标，这两个点将用于绘制线段

    canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill="black", width=1)
    # 在画布上创建一条线段，连接 dot1 和 dot2
    # dot1[0] 和 dot1[1] 是第一个点的 x 和 y 坐标
    # dot2[0] 和 dot2[1] 是第二个点的 x 和 y 坐标
    # "fill" 指定线段的颜色为黑色
    # "width" 指定线段的宽度为 1 像素


# 绘制多边形边界
# 定义绘制多边形边界的函数
def draw_edges():
    global points, flagPolygon, canvas, flagPolygonExist
    # 使用全局变量 points, flagPolygon, canvas 和 flagPolygonExist

    if len(points) != 0:
        # 如果 points 列表不为空（包含至少一个点）
        for i in range(len(points) - 1):
            # 遍历 points 列表中的点，从第一个点到倒数第二个点
            dot1 = points[i]
            dot2 = points[i + 1]
            # 获取相邻的两个点的坐标

            canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill="black", width=1)
            # 在画布上创建一条线段，连接 dot1 和 dot2
            # dot1[0] 和 dot1[1] 是第一个点的 x 和 y 坐标
            # dot2[0] 和 dot2[1] 是第二个点的 x 和 y 坐标
            # "fill" 指定线段的颜色为黑色
            # "width" 指定线段的宽度为 1 像素

        # 绘制多边形的最后一条边，连接最后一个点和第一个点，完成多边形
        canvas.create_line(points[0][0], points[0][1], points[-1][0], points[-1][1], fill="black", width=1)

        flagPolygon = False
        # 将 flagPolygon 设置为 False，取消绘制多边形
        flagPolygonExist = True
        # 将 flagPolygonExist 设置为 True，表示多边形已存在


# 清除画布
def clean():
    global canvas, flagPolygonExist
    flagPolygonExist = False
    points.clear()
    canvas.delete("all")


# 移动多边形
# 定义点击移动按钮的函数
def clickMove():
    global dx, dy
    # 使用全局变量 dx 和 dy

    if flagPolygonExist:
        # 如果存在多边形（flagPolygonExist 为 True）

        window = Tk()
        # 创建一个新的顶级窗口

        x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2 + 200
        y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2 - 100
        # 计算新窗口的位置坐标

        window.wm_geometry("+%d+%d" % (x, y))
        # 设置新窗口的位置
        window.grab_set()
        # 使新窗口获取输入焦点
        window.resizable(False, False)
        # 禁止改变新窗口的大小
        window.title("Сместить")
        # 设置新窗口的标题为 "Сместить"
        window.geometry("200x100")
        # 设置新窗口的大小为 200x100 像素

        label = tk.Label(window, text="Введите смещение:")
        # 创建一个标签，显示 "Введите смещение:"

        text_dx = tk.IntVar()
        text_dy = tk.IntVar()
        # 创建整数类型的 Tkinter 变量

        entry_dx = tk.Entry(window, textvariable=text_dx)
        entry_dy = tk.Entry(window, textvariable=text_dy)
        # 创建两个文本输入框，分别与 text_dx 和 text_dy 变量关联

        btn = tk.Button(window, text="Готово", command=window.destroy)
        # 创建一个按钮，显示 "Готово"，点击后执行 window.destroy 关闭窗口

        label.grid(row=0, columnspan=2)
        # 将标签放置在窗口的第 0 行，并占据 2 列的空间
        tk.Label(window, text="dx:").grid(row=1, column=0)
        # 创建一个标签显示 "dx:"，放置在窗口的第 1 行，第 0 列
        tk.Label(window, text="dy:").grid(row=2, column=0)
        # 创建一个标签显示 "dy:"，放置在窗口的第 2 行，第 0 列
        entry_dx.grid(row=1, column=1)
        # 将 dx 的文本输入框放置在窗口的第 1 行，第 1 列
        entry_dy.grid(row=2, column=1)
        # 将 dy 的文本输入框放置在窗口的第 2 行，第 1 列
        btn.grid(row=3, columnspan=2)
        # 将 "Готово" 按钮放置在窗口的第 3 行，并占据 2 列的空间

        dx = int(text_dx.get())
        dy = int(text_dy.get())
        # 从文本输入框中获取用户输入的 dx 和 dy 的值，将它们存储到全局变量 dx 和 dy 中


# 移动多边形
# 定义移动多边形的函数
def move():
    global points, dx, dy, FlagClicMove
    # 使用全局变量 points, dx, dy 和 FlagClicMove

    canvas.delete("all")
    # 清空画布上的所有内容

    ddx = dx - points[0][0]
    ddy = dy - points[0][1]
    # 计算 dx 和 dy 与多边形的第一个顶点的偏移量

    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        # 获取多边形的每个顶点的坐标

        points[i][0] = x + ddx
        points[i][1] = y + ddy
        # 更新每个顶点的坐标，实现平移

    draw_edges()
    # 调用 draw_edges 函数来重新绘制更新后的多边形边界


# 注释：
# 这个函数用于实现多边形的平移操作。首先，它计算出多边形的第一个顶点与用户指定的目标位置 (dx, dy) 之间的偏移量（ddx 和 ddy）。
# 然后，它遍历多边形的每个顶点，将每个顶点的坐标按照偏移量进行更新，从而实现多边形的平移操作。
# 最后，它调用 draw_edges 函数，重新绘制更新后的多边形边界，以在画布上显示平移后的多边形。

# 旋转多边形
# 定义旋转多边形的函数
def rotate():
    global points, a, canvas, dx, dy
    # 使用全局变量 points, a, canvas, dx, dy

    ddx = sum([k[0] for k in points]) // len(points)
    ddy = sum([k[1] for k in points]) // len(points)
    # 计算多边形所有顶点的平均坐标，作为旋转中心

    for i in range(len(points)):
        # 遍历多边形的每个顶点
        first_matrix = [points[i][0], points[i][1], 1]
        # 创建一个长度为3的一维数组，存储当前顶点的坐标和一个常数1

        second_matrix = [[math.cos(a), math.sin(a), 0],
                         [-1 * math.sin(a), math.cos(a), 0],
                         [-1 * points[i][0] * math.cos(a) + points[i][1] * math.sin(a) + points[i][0],
                          -1 * points[i][0] * math.sin(a) - points[i][1] * math.cos(a) + points[i][1], 1]]
        # 创建一个3x3的矩阵，表示旋转变换矩阵

        length = len(first_matrix)
        result_matrix = [0 for i in range(length)]
        # 创建一个与第一个矩阵相同长度的一维数组，用于存储结果矩阵

        for m in range(length):
            for j in range(length):
                result_matrix[m] += first_matrix[m] * second_matrix[j][m]
                # 计算矩阵相乘的结果

        x = points[i][0]
        y = points[i][1]
        points[i][0] = x * math.cos(a) + y * math.sin(a)
        points[i][1] = (-1) * x * math.sin(a) + y * math.cos(a)
        # 更新多边形顶点坐标，实现旋转


# 注释：
# 这个函数用于实现多边形的旋转操作。首先，它计算多边形所有顶点的平均坐标，作为旋转中心。
# 然后，它遍历多边形的每个顶点，将每个顶点的坐标应用旋转矩阵进行计算，从而实现多边形的旋转操作。
# 最后，它更新多边形顶点的坐标，实现旋转操作。

# 缩放多边形
# 定义一个函数用于缩放多边形
def resize():
    global points, k
    sum_x = sum([k[0] for k in points]) // len(points)  # 计算多边形顶点的x坐标总和
    sum_y = sum([k[1] for k in points]) // len(points)  # 计算多边形顶点的y坐标总和
    canvas.delete("all")  # 清空画布上的所有内容
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        points[i][0] = (x - sum_x) // k + sum_x  # 缩放多边形的x坐标
        points[i][1] = (y - sum_y) // k + sum_y  # 缩放多边形的y坐标


k = 0.5  # 缩放比例

root = tk.Tk()  # 创建主窗口

# 计算窗口位置使其居中
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 250
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 250
root.wm_geometry("+%d+%d" % (x, y))
root.resizable(False, False)  # 禁止窗口大小调整
root.title("lab4")  # 设置窗口标题

canvas = tk.Canvas(root, width=500, height=500)  # 创建画布
canvas.pack()  # 将画布添加到窗口中

a = 30  # 用于设置多边形的顶点数

dx, dy = 0, 0  # 用于移动多边形的增量

# 绑定鼠标左键点击事件到draw函数
canvas.bind("<Button-1>", draw)

# 创建按钮，设置文本为"绘制点"，并绑定到fDot函数
btn1 = tk.Button(root, text="绘制点")
btn1.config(command=fDot)
btn1.pack(side="left")

# 创建按钮，设置文本为"绘制多边形"，并绑定到fPolygon函数
btn3 = tk.Button(root, text="绘制多边形")
btn3.config(command=fPolygon)
btn3.pack(side="left")

# 创建按钮，设置文本为"绘制多边形边界"，并绑定到draw_edges函数
btn3 = tk.Button(root, text="绘制多边形边界")
btn3.config(command=draw_edges)
btn3.pack(side="left")

# 创建按钮，设置文本为"移动多边形"，并绑定到move函数
btn2 = tk.Button(root, text="移动多边形")
btn2.config(command=move)
btn2.pack(side="left")

# 创建按钮，设置文本为"旋转多边形"，并绑定到rotate函数
btn2 = tk.Button(root, text="旋转多边形")
btn2.config(command=rotate)
btn2.pack(side="left")

# 创建按钮，设置文本为"缩放多边形"，并绑定到resize函数
btn2 = tk.Button(root, text="缩放多边形")
btn2.config(command=resize)
btn2.pack(side="left")

# 创建按钮，设置文本为"清空"，并绑定到clean函数
btn4 = tk.Button(root, text="清空")
btn4.config(command=clean)
btn4.pack(side="left")

root.mainloop()  # 进入Tkinter的主事件循环，等待用户操作
