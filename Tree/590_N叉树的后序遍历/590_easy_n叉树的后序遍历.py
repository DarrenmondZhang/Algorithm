#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/description/
#
# algorithms
# Easy (74.03%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    28.9K
# Total Submissions: 39K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的后序遍历。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其后序遍历: [5,6,3,2,4,1].
# 
# 
# 
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = [root]
        res = []

        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
            for c in root.children:
                stack.append(c)
        return res[::-1]

# @lc code=end

