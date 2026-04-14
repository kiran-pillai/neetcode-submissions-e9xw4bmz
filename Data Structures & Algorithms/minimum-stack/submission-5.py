class MinStack:

    def __init__(self):
        self.stack=[]
        self.prefix=[]


    def getLastIndex(self) -> int:
        return len(self.stack)-1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.prefix.append(val) if len(self.prefix)==0 else self.prefix.append(min(self.prefix[-1],val))
      
    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
"""
top: 2
"""
