'''
奇偶排序算法
分别对奇数项和偶数项的每一个元素，进行前后比较。
'''
import random
import datetime


def swap(array, ele1, ele2):
    temp = array[ele1]
    array[ele1] = array[ele2]
    array[ele2] = temp


class OddEvenSort(object):

    def __init__(self):
        self.array = []
        self.nums = 0

    def add_ele(self, element):
        self.array.append(element)
        self.nums += 1
        return self

    def travel_array(self):
        return [x for x in self.array]


def odd_even_sort(array):
    for i in range(0, len(array) // 2):

        for j in range(0, len(array) - i - 1):
            if j % 2 == 1:
                # 奇数项进行排序
                if array[j] > array[j + 1]:
                    swap(array, j, j + 1)

            if j % 2 == 0:
                # 偶数项进行排序
                if array[j] > array[j + 1]:
                    swap(array, j, j + 1)


if __name__ == "__main__":
    odd_sort = OddEvenSort()
    for i in range(0, 10000):
        odd_sort.array.append(random.randint(0, 10000))
    r = odd_sort.travel_array()
    print(r)
    start = datetime.datetime.now()
    odd_even_sort(r)
    end = datetime.datetime.now()
    print(r)
    print("总共花费时间:", end - start)
