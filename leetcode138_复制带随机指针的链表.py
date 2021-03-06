# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
#
# 要求返回这个链表的 深拷贝。 
#
# 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
#
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。


class Node:
    def __init__(self, x, next, random):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head: return None
        # 复制节点
        cur = head
        while cur:
            # 保存下一个节点
            tmp = cur.next
            # 后面跟着同样的节点
            cur.next = Node(cur.val, None, None)
            # 拼接
            cur.next.next = tmp
            cur = tmp
        # 复制random指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分
        cur = head
        copy_head = head.next
        copy_cur = copy_head
        while copy_cur.next:
            # 组head
            cur.next = cur.next.next
            cur = cur.next
            # 组 copy_head
            copy_cur.next = copy_cur.next.next
            copy_cur = copy_cur.next
        # 把链表结束置空
        cur.next = copy_cur.next
        copy_cur.next = None
        return copy_head

