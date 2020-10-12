'''
选择排序算法思想
先将0号位置做为最小值，简称哨兵，然后将哨兵从右边的无序队列中比较出一个最小的与之交换，即选择最小的与哨兵交换。
下一次比较时，再重新以左边第二位当做哨兵，再从右边无序序列中与第二个哨兵进行比较，以此类推，直至左边成一个完整的有序序列。
一句话总结: 就是每次总是从哨兵和无序队列中所有元素中，选择最小的那一位当做新的哨兵。
'''


def swap(array, ele1, ele2):
    temp = array[ele1]
    array[ele1] = array[ele2]
    array[ele2] = temp


def selection_sort(array):
    for i in range(0, len(array)):
        min_val = array[i]
        for j in range(i, len(array)):
            if min_val > array[j]:
                swap(array, i, j)
    return array


class SelectionSort(object):

    def __init__(self):
        self.array = []
        self.length = 0

    def add_element(self, element):
        self.array.append(element)
        self.length += 1
        return self

    def travel_array(self):
        return [x for x in self.array]


if __name__ == "__main__":
    selection = SelectionSort()
    selection.add_element(2).add_element(1).add_element(1).add_element(3).add_element(5).add_element(1).add_element(
        10).add_element(2)
    re = selection.travel_array()
    print(re)
    # 选择排序
    result = selection_sort(re)
    print("排序后的结果为:", result)
