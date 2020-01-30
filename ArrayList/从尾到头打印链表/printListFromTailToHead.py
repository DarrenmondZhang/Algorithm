class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printListFromTailToHead(listNode):
    """
    返回从尾部到头部的列表值序列，例如[1,2,3]
    :param listNode:
    :return:
    """
    pTmp = listNode
    ret_array = []
    while pTmp:
        ret_array.insert(0, pTmp.val)  # 每次都往临时数组的头部添加
        pTmp = pTmp.next
    print(ret_array)
    return ret_array


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
    printListFromTailToHead(l1)
