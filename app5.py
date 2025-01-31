import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, lambdify


def plot_function():
    func_expr = input("请输入函数解析式（例如：x^2 + 3*x + 2）：")

    # 将字符串形式的函数解析式转换为SymPy表达式 <---- AI 说的我也没懂，好像是只有sympify之后才能绘制
    func_expr = sympify(func_expr)

    # 定义自变量范围
    x_min = float(input("请输入自变量范围的最小值："))
    x_max = float(input("请输入自变量范围的最大值："))
    x = np.linspace(x_min, x_max, 100000)  # np.linspace意思是在（从a, 到b的范围内, 绘制共____个点）

    # 将SymPy表达式转换为可调用的函数 <---- AI 说的我也没懂，感觉应该是sympify之后py识别不了所以又要变成lanbdify的形式
    func = lambdify('x', func_expr, 'numpy')#(变量， 想要lambdify的变量，模块（numpy适合处理数组和大规模数值运算，math适合处理单个数值）)

    # 赋值
    y = func(x)

    # 绘制图像
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph')
    plt.grid(True)
    plt.show()


plot_function()

