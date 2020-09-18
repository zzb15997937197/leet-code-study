# 全排列
a = [1, 2, 3, 4, 5, 2]
'''
12345
.
.
.
54321
先reversed,然后再list
列表反转list(reversed(a))

'''
# 排序
a = list(sorted(a))
print(a)

# 反转
a = list(reversed(a))
print(a)

b = ""
for i in a:
    b = b + str(i)
print(b)
