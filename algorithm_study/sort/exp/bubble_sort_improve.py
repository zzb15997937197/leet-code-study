'''
冒泡排序双向移动，将大数往右边移动，小的数往左边移动
'''

'''
冒泡排序，写一个冒泡排序
1. 初始化一个类，包含一个数组和元素总数
2. 能对数组的元素进行插入，遍历的方法
'''


def swap(array, ele1, ele2):
    temp = array[ele1]
    array[ele1] = array[ele2]
    array[ele2] = temp


# 大的数往右侧移动,外循环从大到小
def bubble_sort(array):
    for i in range(len(array) - 1, -1, -1):
        for j in range(0, i):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)


# 大的数往左侧移动，外循环从小到大。
def left_bubble_sort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] < array[j + 1]:
                swap(array, j, j + 1)


# 冒泡排序算法改进
def improve_bubble_sort(array):
    times = len(array) // 2
    for i in range(0, times):
        # i的右边
        for j in range(i, len(array) - i - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)

        # i的左边
        for k in range(0, i):
            if array[k] > array[k + 1]:
                swap(array, k, k + 1)


# 双向冒泡排序
def improve_bubble_sort_two_way(array):
    print("双向冒泡排序")
    left = 0
    right = len(array) - 1
    while left < right:
        for i in range(left + 1, len(array)):
            # 向左冒泡
            if array[left] > array[i]:
                swap(array, left, i)
        left += 1

        if left >= right:
            break
        for j in range(right, -1, -1):
            # 向右冒泡
            if array[right] < array[j]:
                swap(array, right, j)
        right -= 1
    return array


'''
以上两种方式，都是从0位到未排序好的那一位之间的元素之间，进行两两比较，有一边倒的趋势。
'''


class ArrayBub(object):

    def __init__(self):
        self.array = []
        self.nums = 0

    def add_ele(self, element):
        self.array.append(element)
        self.nums += 1
        return self

    def travel_array(self):
        return [x for x in self.array]


if __name__ == "__main__":
    print()
    bubble = ArrayBub()
    bubble.add_ele(3).add_ele(2).add_ele(1).add_ele(5).add_ele(9).add_ele(1)
    r = bubble.travel_array()
    print(r)
    improve_bubble_sort_two_way(r)
    print("排序后的结果为:", r)
