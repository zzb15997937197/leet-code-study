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


'''
奇偶排序算法，每次拿出数组中的奇数项和后一项进行比较，同时拿出数组中的偶数项和后一项进行比较
结束的条件: 没有进行交换了。 当奇数项和偶数项有交换的时候将奇数排序的odd_flag=false,even_flag=false，
如果都没有进行交换，表示已经排序完毕，那么odd_flag=True,even_flag=True
'''


def odd_even_sort(array):
    odd_flag = False
    even_flag = False
    while not odd_flag or not even_flag:
        odd_flag = True
        even_flag = True
        # 奇数项排序
        base = 0
        for odd in range(base, len(array) - 1, 2):
            if array[odd] > array[odd + 1]:
                swap(array, odd, odd + 1)
                odd_flag = False
        # 偶数项排序
        base = 1
        for even in range(base, len(array) - 1, 2):
            if array[even] > array[even + 1]:
                swap(array, even, even + 1)
                even_flag = False


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
