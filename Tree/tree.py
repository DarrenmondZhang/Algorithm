class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归形式
def preOrderRecusive(root):
    """先根遍历
    :param root: tree
    :return:
    """
    if root is None:
        return None
    print(root.val)
    preOrderRecusive(root.left)
    preOrderRecusive(root.right)


def midOrderRecusive(root):
    """中根遍历
    :param root: tree
    :return:
    """
    if root is None:
        return None
    midOrderRecusive(root.left)
    print(root.val)
    midOrderRecusive(root.right)


def latOrderRecusive(root):
    """后根遍历
    :param root: tree
    :return: 后根遍历的值
    """
    if root is None:
        return None
    latOrderRecusive(root.left)
    latOrderRecusive(root.right)
    print(root.val)


# 非递归形式：递归和循环可以相互转换；跟栈结构很像
# 非递归形式都可以将递归的内容以栈的形式转换成非递归形式。
def preOrder(root):
    if root is None:
        return None
    stack = []  # 栈
    tmpNode = root
    while tmpNode or stack:
        while tmpNode:
            print(tmpNode.val)
            stack.append(tmpNode)
            tmpNode = tmpNode.left

        node = stack.pop()
        tmpNode = node.right


# 对于深度优先： 先序遍历 中序遍历 后序遍历
if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t6.right = t8
    #
    # preOrderRecusive(t1)
    # print('--' * 30)
    # midOrderRecusive(t1)
    # print('--' * 30)
    # latOrderRecusive(t1)
    # print('--' * 30)

    preOrder(t1)