class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        new_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, new_min))

    def pop(self) -> None:
        val = self.stack.pop()

    def top(self) -> int:
        return None if not self.stack else self.stack[-1][0]

    def getMin(self) -> int:
        return None if not self.stack else self.stack[-1][1]
