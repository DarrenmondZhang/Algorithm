class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def ReverseList(pHead):
    """输入一个链表，反转链表后，输出新链表的表头。
    :param pHead:
    :return:
    """
    left_node = pHead
    mid_node = left_node.next
    right_node = mid_node.next

    if pHead is None:
        return None
    if pHead.next is None:
        return pHead

    left_node.next = None
    while right_node is not None:
        mid_node.next = left_node
        left_node = mid_node
        mid_node = right_node
        right_node = right_node.next

    mid_node.next = left_node
    print(mid_node.val)
    return mid_node


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    ReverseList(l1)

