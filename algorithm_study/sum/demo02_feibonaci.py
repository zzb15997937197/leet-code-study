# 费波纳茨数列问题 1 1 2 3 5
# 1. 找出斐波那次数列第n项问题
from distlib.compat import raw_input

n = raw_input("请输入斐波那次数列结束的位置:")


def func(number):
    if number == 1 or number == 2:
        return 1
    else:
        return func(number - 1) + func(number - 2)


res = func(int(n))
print("位置为" + n + "的值为:" + str(res))

# 2. 求斐波那次数列前n项和
data = [1, 1]


def func_sum(number):
    if number == 1 or number == 2:
        return 1
    else:
        last_one = func_sum(number - 1)
        last_two = func_sum(number - 2)
        if last_one not in data and last_one > 1:
            data.append(last_one)
        if last_two not in data and last_two > 1:
            data.append(last_two)
        return last_one + last_two


data.append(func_sum(int(n)))
print("位置为" + n + "的总和为:" + str(sum(data)))
print(data)
