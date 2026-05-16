class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
    def push(self, val: int) -> None:
        if not self.min or val<=self.min[-1]:
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack):
            top = self.stack.pop()
            if self.min[-1] == top:
                self.min.pop()
        else:
            return None

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) else None

    def getMin(self) -> int:
        return self.min[-1] if len(self.min) else None
        
