class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 迭代
    def postorderTraversal(self, root):
        stack = [(root, False)]
        res = []
        while stack:
            node, flag = stack.pop()
            if node:
                if flag:
                    res.append(node.val)
                else:
                    stack.append((node,True))
                    stack.append((node.right,False))
                    stack.append((node.left,False))
        return res


class Solution1:
    # 递归
    def postorderTraversal(self, root):
        res = []

        def helper(root):
            if not root:
                return None
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        helper(root)
        return res
