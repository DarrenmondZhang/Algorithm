#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (72.12%)
# Likes:    586
# Dislikes: 0
# Total Accepted:    195.7K
# Total Submissions: 271.2K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # if not root:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        res = []
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

# @lc code=end

