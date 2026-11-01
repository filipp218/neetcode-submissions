class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack_min:
            self.stack_min.append(val)
        else:
            if self.stack_min[-1] > val:
                self.stack_min.append(val)
            else:
                min_val = self.stack_min[-1]
                self.stack_min.append(min_val)


    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if self.stack_min:
            return self.stack_min[-1]
        return -1
