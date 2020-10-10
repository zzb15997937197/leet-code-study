'''
使用python实现一个链表，需要具备如下功能:
1. 可以在头部、尾部或者指定位置插入节点。
2. 遍历链表。
'''


# 初始化一个节点
class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkedList(object):

    def __init__(self):
        self.header = None
        self.length = 0

    # 判断链表是否为空,数值使用==比较，对象使用is来判断是否为None即可。
    def is_empty(self):
        if self.header is None:
            return True
        else:
            return False

    # 在链表头部插入元素
    def add_node_from_head(self, node):
        if self.header is None:
            self.header = node
        else:
            node.next = self.header
            # 在头部插入，那么新插入的节点成为了新的头节点
            self.header = node
        self.length += 1
        return self

    # 在链表尾部插入元素
    def add_node_from_behind(self, node):
        current_node = self.header
        if self.is_empty():
            self.add_node_from_head(node)
        else:
            # 一直遍历到尾部节点
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1
        return self

    # 在指定位置节点前插入一个新的节点,下标从0开始
    '''
      插入的节点的前一个节点的next指向新的节点，新的节点的next指向前一个节点之前指向的节点
    '''

    def add_node_index(self, node, index):
        if self.is_empty():
            self.header = node
            self.length = 1
            return self
        if index > self.length - 1 or index < 0:
            print("超出范围,插入失败!")
            return self
        else:
            current_node = self.header
            count = 0
            while True:
                if current_node is not None:
                    # 最少有2个节点
                    if count == index:
                        print("...找到位置....")
                        if count == 0:
                            # 插入到头节点之前
                            node.next = current_node
                            self.header = node
                        else:
                            node.next = current_node
                            last_node.next = node
                        self.length += 1
                        return self
                    else:
                        count += 1
                        last_node = current_node
                        current_node = current_node.next
                else:
                    # 只有一个头节点
                    node.next = current_node
                    self.header = node
                    self.length += 1
                    return self

    # 遍历链表
    def traversing_list(self):
        header_node = self.header
        result = ",val:" + str(header_node.val)
        while header_node.next is not None:
            result = result + "-->" + ",val:" + str(header_node.next.val)
            temp = header_node
            header_node = header_node.next
            if temp == header_node:
                print("出现自己指向自己的问题！")
                return
        print("链表为:", result, ",长度为:" + str(self.length))


if __name__ == '__main__':
    print("初始化一个链表!")
    header = Node(0)
    linked_list = SingleLinkedList()
    linked_list.add_node_index(header, 0)
    linked_list.traversing_list()
    node0 = Node(1)
    # 添加同一个对象会出现自己指向自己的问题
    # linked_list.add_node_from_head(header)
    linked_list.add_node_from_head(node0)
    linked_list.traversing_list()
    # 再头部加2个节点
    node1 = Node(2)
    node2 = Node(3)
    linked_list.add_node_from_head(node1).add_node_from_head(node2)
    linked_list.traversing_list()
    node3 = Node(4)
    linked_list.add_node_from_behind(node3)
    linked_list.traversing_list()
    # 在index=2处插入一个节点
    node4 = Node(5)
    linked_list.add_node_index(node4, 0)
    linked_list.traversing_list()
