# 全排列，给定一个没有重复数字的序列，返回其所有的全排列

'''

解题思想: 固定第一个元素，然后后面的元素再进行全排列。
然后再固定第二个元素，对后面的元素再进行全排列。

'''


def permutations(arr, position, end):
    if position == end:
        return arr
    else:
        for index in range(position, end):
            print("origin:", arr)
            arr[index], arr[position] = arr[position], arr[index]
            print("互换位置后:", arr)
            target = permutations(arr, position + 1, end)
            if target is not None:
                print("target:", target)
            print("全排列后:", arr)
            arr[index], arr[position] = arr[position], arr[index]
            print("恢复位置:", arr)

        '''
         position=0
        
        '''


arr = ["a", "b", "c"]
permutations(arr, 0, len(arr))

# import random
#
# a = [1, 6, 3, 4, 5]
#
#
# def factorial(n):
#     result = n
#     for i in range(1, n):
#         result *= i
#     return result
#
#
# def generate_num(a):
#     print("生成随机组成的六位数")
#     target = ""
#     for i in range(len(a)):
#         index = random.randrange(0, len(a))
#         target = target + a[index]
#
#
# def full_arrangement(a):
#     total = factorial(len(a))
#     print("total:", total)
#     result = []
#     start = list(sorted(a))
#     end = list(reversed(start))
#     start_str = [str(i) for i in start]
#     end_str = [str(i) for i in end]
#     start_str = "".join(start_str)
#     end_str = "".join(end_str)
#     print("start:", start_str, "\nend:", end_str)
#     while True:
#         target = 0
#         if int(start_str) <= target <= int(end_str):
#             print("根据a生成任意不重复的随机数组合")
#             t = generate_num(a)
#             if t not in result:
#                 result.append(t)
#
#             if len(result) == total:
#                 return result
#
#     return result
#
#
# result = full_arrangement(a)
# print(result)
#
#
#
