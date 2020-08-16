# 链接：https://www.acwing.com/problem/content/1453/
# 来源：旷世

# 给定一个单链表，请使用快速排序算法对其排序。

# 要求：期望平均时间复杂度为 O(nlogn)，期望额外空间复杂度为 O(logn)。

# 思考题： 如果只能改变链表结构，不能修改每个节点的val值该如何做呢？

# 数据范围
# 链表中的所有数大小均在 int 范围内，链表长度在 [0,10000]。

# 输入样例：
# [5, 3, 2]
# 输出样例：
# [2, 3, 5]

###################### code beginning #################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def quickSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        leftNode, midNode, rightNode = ListNode(-1), ListNode(-1), ListNode(-1)
        # 由于需要在链表尾部插入节点，定义尾部节点
        leftTail, midTail, rightTail = leftNode, midNode, rightNode
        p, p_val = head, head.val

        while p:
            if p.val < p_val:
                leftTail.next = p
                leftTail = leftTail.next
            elif p.val == p_val:
                midTail.next = p
                midTail = midTail.next
            else:
                rightTail.next = p
                rightTail = rightTail.next
            p = p.next
        # 将列表的尾部插入None，否则不知道什么时候链表结束
        leftTail.next = midTail.next = rightTail.next = None

        # 对左右两边链表进行递归，left.next是真实结点
        leftNode.next = self.quickSortList(leftNode.next)
        rightNode.next = self.quickSortList(rightNode.next)

        # 拼接三个链表
        self.get_tail(leftNode).next = midNode.next
        self.get_tail(leftNode).next = rightNode.next
        
        # print(leftNode.next.val)
        return leftNode.next
    
    def get_tail(self, head):
        while head.next:
            head = head.next
        return head

Node1 = ListNode(5)
Node2 = ListNode(3)
Node3 = ListNode(2)
Node1.next = Node2
Node2.next = Node3
Solution().quickSortList(Node1)