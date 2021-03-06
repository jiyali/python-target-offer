# 题目：请实现两个函数，分别用来序列化和反序列化二叉树
#       二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
#             序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，
#             序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。
#       二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

# 思路：序列化：前序遍历二叉树的节点，遇到空节点则设置为'#'
#       反序列化：遍历字符串


class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    flag = -1

    def Serialize(self, root):
        # write code here
        # 前序遍历输出序列
        if root is None:
            return '#'

        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        self.flag += 1

        l = s.split(',')

        if self.flag > len(s) - 1:
            return None

        # 如果序列是‘#’，则节点设置为None
        root = None

        # 如果序列不是'#'，添加新的节点
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)

        return root


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = None
node3.left = node5
node3.right = node6

s = Solution()
print(s.Serialize(node1))
