# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 is None or pRoot1 is None:
            return False

        def hasEqual(pRoot1, pRoot2):
            if pRoot1 is None:
                return False
            if pRoot1.val == pRoot2.val:
                if pRoot2.left is None:
                    leftEqual = True
                else:
                    leftEqual = hasEqual(pRoot1.left, pRoot2.left)
                if pRoot2.right is None:
                    rightEqual = True
                else:
                    rightEqual = hasEqual(pRoot1.right, pRoot2.right)
                return leftEqual and rightEqual
            return False

        if pRoot2.val == pRoot1.val:
            ret = hasEqual(pRoot1, pRoot2)
            if ret:
                return True

        ret = self.HasSubtree(pRoot1.left, pRoot2)
        if ret:
            return True

        ret = self.HasSubtree(pRoot1.right, pRoot2)
        return ret


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)

    t9 = TreeNode(3)
    t10 = TreeNode(6)
    t11 = TreeNode(7)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t6.right = t8

    t9.left = t10
    t9.right = t11

    s = Solution()
    print(s.HasSubtree(t1, t9))
