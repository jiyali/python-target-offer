# 创建一个辅助最小栈
import math


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = [math.inf]  # 辅助栈

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.stack2.append(min(x, self.stack2[-1]))

    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]
