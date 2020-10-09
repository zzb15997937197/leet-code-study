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

    # 遍历链表
    def traversing_list(self):
        header = self.header
        result = ",val:" + str(header.val)
        while header.next is not None:
            result = result + "-->" + ",val:" + str(header.next.val)
            header = header.next
        print("链表为:", result, ",长度为:" + str(self.length))


if __name__ == '__main__':
    print("初始化一个链表!")
    header = Node(1)
    linked_list = SingleLinkedList()
    linked_list.add_node_from_head(header)
    linked_list.traversing_list()
    # 再头部加2个节点
    node1 = Node(2)
    node2 = Node(3)
    linked_list.add_node_from_head(node1).add_node_from_head(node2)
    linked_list.traversing_list()
    node3 = Node(4)
    linked_list.add_node_from_behind(node3)
    linked_list.traversing_list()
