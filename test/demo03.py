# 给定4个数[1,3,5,9]全排列为
# 参考博客: https://www.cnblogs.com/lrheisoo/p/7124898.html
'''
1 3 5 9
1 3 9 5
1 5 3 9
1 5 9 3
1 9 3 5
1 9 5 3
3 1 5 9
3 1 9 5
3 5 1 9
3 5 9 1
3 9 1 5
3 9 5 1
'''

from itertools import permutations

a = [1, 3, 5, 7, 9]
permutation = permutations(a)
for i in permutation:
    print(i)

