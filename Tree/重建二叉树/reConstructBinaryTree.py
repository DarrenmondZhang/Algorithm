# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        elif len(pre) != len(tin):
            return None
        else:
            # 取出pre的值
            root = pre[0]
            rootNode = TreeNode(root)
            pos = tin.index(root)

            tinLeft = tin[:pos]
            tinRight = tin[pos + 1:]

            preLeft = pre[1:pos + 1]
            preRight = pre[pos + 1:]

            leftNode = self.reConstructBinaryTree(preLeft, tinLeft)
            rightNode = self.reConstructBinaryTree(preRight, tinRight)

            if leftNode:
                rootNode.left = leftNode
            if rightNode:
                rootNode.right = rightNode
            return rootNode
