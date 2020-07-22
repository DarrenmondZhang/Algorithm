#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (65.90%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    24.9K
# Total Submissions: 37.8K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其层序遍历:
# 
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
# 
# 
# 
# 
# 说明:
# 
# 
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = collections.deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        return result


# @lc code=end

