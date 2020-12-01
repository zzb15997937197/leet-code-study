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


## 方法三:  if..else可用三元表达式替换 x if y else z  , 如果y为真，那么取x,否则取z

def func(number):
    return 0 if len(number) == 0 else number[0] + func(number[1:])


print(func([1, 2, 3, 4, 5, 10]))

## 方法4,使用while循环完成求和
a = [1, 2, 3, 4, 5, 16]
sum_data = 0
while a:
    sum_data += a[0]
    a = a[1:]
print(sum_data)

# 可以发现，如果在简单求和的情况下，使用while或for循环也能够发挥出不错的效果。
# 每次递归会在堆栈上生成一个本地作用域副本，对于简单可使用for循环进行替代,如果是比较多的嵌套，那么for循环就不适用了。
# 如: 求所有列表里的元素和: [1,2,3,[4,5,[6,7,8]],[9,10]]
