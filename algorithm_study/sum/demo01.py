# 递归求和,传一个列表，怎么使用递归求和
# 方法一: 自己写递归方法求解
def func(number):
    if len(number) == 0:
        return 0
    else:
        return number[0] + func(number[1:])


sum_data = func([1, 2, 3, 4, 5, 6])
print(sum_data)

# 方法二:

print(sum([1, 2, 3, 4, 5]))
