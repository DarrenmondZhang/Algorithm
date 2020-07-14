#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (57.86%)
# Likes:    622
# Dislikes: 0
# Total Accepted:    79.9K
# Total Submissions: 129.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 
# 
# 示例：
# 
# 给你这个链表：1->2->3->4->5
# 
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 
# 
# 
# 说明：
# 
# 
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        start = dummy

        while start:
            # 设置end结点，看是否够k个一组
            end = start
            for i in range(k):
                end = end.next
                if not end:
                    return dummy.next
            
            # swap node
            swap_a = start.next
            swap_b = swap_a.next
            for i in range(k - 1):
                temp = swap_b.next
                swap_b.next = swap_a
                swap_a = swap_b
                swap_b = temp
            temp = start.next
            start.next = swap_a
            temp.next = swap_b
            start = temp
        return dummy.next
        


        
# @lc code=end

