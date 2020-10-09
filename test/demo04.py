import math

# 1. math.log() 函数，能够计算出一个整数它有多少位。
a = 15678
x = int(math.log(a, 10)) + 1
print(x)

# 2. pow() 函数，表示x**y次方
print(pow(10, 2))
print(pow(10, 0))

# 3. range(a,b)
print([x for x in range(1, 10)])

# % 表示取余
print(12345 % 1000)
