# 给定4个数[1,3,5,9]全排列为
# 参考博客: https://www.cnblogs.com/lrheisoo/p/7124898.html
'''
a=[1,2,3]
'''

from itertools import permutations

a = [1, 3, 5, 7, 9]
permutation = permutations(a)
for i in permutation:
    print(i)
