class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        return None

    def pop(self) -> None:
        self.stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        self.min = self.stack[0]
        
        for num in self.stack:
            if num < self.min:
                self.min = num
                
        return self.min