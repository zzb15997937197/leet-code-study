'''
插入排序算法分析
使用列表来实现
'''


def swap(array, ele1, ele2):
    temp = array[ele1]
    array[ele1] = array[ele2]
    array[ele2] = temp


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


if __name__ == "__main__":
    insert_sort = Insertion_sort()
    insert_sort.add_element(1).add_element(6).add_element(2).add_element(1).add_element(10).add_element(8).add_element(
        2)
    array = insert_sort.travel_array()
    print(array)
    for i in range(1, len(array)):
        temp = array[i]
        j = i
        while j > 0 and array[j - 1] >= temp:
            swap(array, j, j - 1)
            # temp与j-1交换位置后，再向前比较,如果小的话，那么就继续向前交换位置
            j = j - 1
    print(array)
