'''
比较三种排序算法的效率
'''
import random
import datetime

from distlib.compat import raw_input


def swap(array, ele1, ele2):
    temp = array[ele1]
    array[ele1] = array[ele2]
    array[ele2] = temp


# 冒泡排序
# 大的数往右侧移动,外循环从大到小
def bubble_sort(array):
    for i in range(len(array) - 1, -1, -1):
        for j in range(0, i):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
    return array


# 大的数往左侧移动，外循环从小到大。
def left_bubble_sort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] < array[j + 1]:
                swap(array, j, j + 1)
    return array


'''
以上两种方式，都是从0位到未排序好的那一位之间的元素之间，进行两两比较，有一边倒的趋势。
'''


def improve_bubble_sort(array):
    times = len(array) // 2
    for i in range(0, times):
        for j in range(i, len(array) - i - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)

        for k in range(0, i):
            if array[k] > array[k + 1]:
                swap(array, k, k + 1)
    return array


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


# 选择排序

def selection_sort(array):
    for out in range(0, len(array)):
        min_val = out
        for j in range(out, len(array)):
            if array[min_val] > array[j]:
                swap(array, min_val, j)
    return array


# 插入排序
def insert_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i
        while j > 0 and array[j - 1] >= temp:
            swap(array, j, j - 1)
            # temp与j-1交换位置后，再向前比较,如果小的话，那么就继续向前交换位置
            j = j - 1
    return array


class ArrayBub(object):

    def __init__(self):
        self.array = []
        self.nums = 0

    def add_ele(self, element):
        self.array.append(element)
        self.nums += 1
        return self

    def remove_ele(self, element):
        self.array.remove(element)
        self.nums -= 1
        return self

    def travel_array(self):
        return [x for x in self.array]

    # 删除所有元素
    def remove_all_elements(self):
        for out in range(0, self.nums):
            self.array.remove(self.array[out])
        return self


if __name__ == "__main__":

    while True:
        bubble = ArrayBub()
        # 初始化10000个随机数进入数组
        for i in range(0, 10000):
            bubble.array.append(random.randint(0, 10000))
        r = bubble.travel_array()
        print(r)
        number = raw_input("please input a number：")
        start = datetime.datetime.now()
        sort_name = ""
        if number == "1":
            print("冒泡排序")
            sort_name = "冒泡排序"
            r = improve_bubble_sort(r)
        elif number == "2":
            print("选择排序")
            sort_name = "选择排序"
            r = selection_sort(r)
        elif number == "3":
            print("插入排序")
            sort_name = "插入排序"
            r = insert_sort(r)
        else:
            print("非法输入!", SystemExit)
        end = datetime.datetime.now()
        print(sort_name + "后的结果为:", r)
        print(sort_name + "花费的总时间为:", end - start)

        ## 结果: 选择排序时间< 插入排序时间< 冒泡排序时间
