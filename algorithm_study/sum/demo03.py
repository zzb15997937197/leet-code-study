# 求n的阶乘
from distlib.compat import raw_input

n = raw_input("请输入n:")


def func(number):
    if number == 1:
        return number
    else:
        return number * func(number - 1)


res = func(int(n))
print(str(n) + "的阶乘为:" + str(res))
