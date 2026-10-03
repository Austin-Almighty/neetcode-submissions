class MinStack:

    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int]= []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.min_stack) != 0:
            curr_min = self.min_stack[-1]
            self.min_stack.append(value if value < curr_min else curr_min)
            return
        self.min_stack.append(value)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop(-1)
            self.min_stack.pop(-1)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return 0

    def getMin(self) -> int:
        return self.min_stack[-1]