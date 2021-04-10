# 求2个整数的最大公约数, 使用辗转相除法，用被除数不断的除余数。将余数当作除数
def max_number(a, b):
    # 定义c为除数，d为大数，为被除数
    if a > b:
        c = b
        d = a
    else:
        c = a
        d = b
    index = d % c
    while index != 0:
        d = c
        c = index
        index = d % c
    return c


target = max_number(18, 30)
print(target)
