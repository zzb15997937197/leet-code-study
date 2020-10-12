'''
冒泡排序，写一个冒泡排序
1. 初始化一个类，包含一个数组和元素总数
2. 能对数组的元素进行插入，遍历的方法
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

    @staticmethod
    def bubble_sort(array, ele1, ele2):
        temp = array[ele1]
        array[ele1] = array[ele2]
        array[ele2] = temp


if __name__ == "__main__":
    print()
    bubble = ArrayBub()
    bubble.add_ele(3).add_ele(2).add_ele(1).add_ele(5).add_ele(9).add_ele(1)
    r = bubble.travel_array()
    print(r)
    for out in range(len(r) - 1, -1, -1):
        for i in range(0, out):
            if r[i] > r[i + 1]:
                bubble.bubble_sort(r, i, i + 1)
    print("排序后的结果为:", r)
