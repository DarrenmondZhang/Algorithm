class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def FindKthToTail(head, k):
    """输入一个链表，输出该链表中倒数第k个结点。
    :param head: 头结点
    :param k: 倒数第k个结点
    :return:
    """
    # 边界条件： k 如果比链表长度大 ，直接返回None
    # K 如果小于链表长度，定义两个变量， 这两个变量中间间隔k
    right_node = head
    left_node = head

    for i in range(k):
        if right_node is None:
            return None
        right_node = right_node.next

    while right_node is not None:
        right_node = right_node.next
        left_node = left_node.next

    print(left_node.val)
    return left_node


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
    FindKthToTail(l1, 5)

