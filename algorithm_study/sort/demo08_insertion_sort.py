'''
插入排序算法分析
使用列表来实现
'''


def swap(array, ele1, ele2):
    temp = array[ele1]
    array[ele1] = array[ele2]
    array[ele2] = temp


def insertion_sort(array):
    for i in range(1, len(array)):
        # 记录当前元素
        temp = array[i]
        # 记录当前元素的下标
        j = i
        # 将当前元素与之前元素的进行比较，前后元素然后进行交换
        while j > 0 and array[j - 1] > temp:
            swap(array, j, j - 1)
            j = j - 1


class Insertion_sort(object):

    def __init__(self):
        self.array = []
        self.length = 0

    def add_element(self, element):
        self.array.append(element)
        self.length += 1
        return self

    def travel_array(self):
        return [x for x in self.array]

    # [1, 6, 2, 1, 10, 8]


'''
插入排序:
1. 将列表中的每一个元素用temp存起来。
2. 然后从temp元素所在的位置与之前的元素进行比较，如果temp元素大于之前的元素，那么就将temp元素插入到之前的有序序列之前。
'''

if __name__ == "__main__":
    insert_sort = Insertion_sort()
    insert_sort.add_element(1).add_element(6).add_element(2).add_element(1).add_element(10).add_element(8).add_element(
        2)
    array = insert_sort.travel_array()
    print(array)
    insertion_sort(array)
    print(array)
