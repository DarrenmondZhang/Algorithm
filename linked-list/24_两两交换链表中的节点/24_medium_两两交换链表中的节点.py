#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (64.92%)
# Likes:    455
# Dislikes: 0
# Total Accepted:    88.3K
# Total Submissions: 135.8K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 为了能够输出结果链表，设置一个空节点，指向头结点
        dummy = ListNode(-1)
        dummy.next = head
        leftNode = dummy

        while head and head.next:
            midNode = head
            rightNode = head.next

            # Swapping
            leftNode.next = rightNode
            midNode.next = rightNode.next
            rightNode.next = midNode

            leftNode = midNode
            head = midNode.next

        return dummy.next
# @lc code=end

