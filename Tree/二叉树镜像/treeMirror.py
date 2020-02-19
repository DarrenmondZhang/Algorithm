# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is None:
            return None

        # 处理根节点
        root.left, root.right = root.right, root.left
        # 处理左子树
        self.Mirror(root.left)
        # 处理右子树
        self.Mirror(root.right)


if __name__ == '__main__':
    t1 = TreeNode(8)
    t2 = TreeNode(6)
    t3 = TreeNode(10)
    t4 = TreeNode(5)
    t5 = TreeNode(7)
    t6 = TreeNode(9)
    t7 = TreeNode(11)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7

    s = Solution()
    print(s.Mirror(t1))
