class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.current_min != [] and val < self.current_min[0]:
            self.current_min.insert(0, val)
        elif self.current_min != [] and val == self.current_min[0]:
            self.current_min.insert(0, val)
        else:
            self.current_min.append(val)

    def pop(self) -> None:
        self.current_min.remove(self.stack[-1])
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min[0]