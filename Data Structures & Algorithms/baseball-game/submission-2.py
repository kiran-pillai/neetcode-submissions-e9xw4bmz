from functools import reduce

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        def isInteger(string: str) -> bool:
            try:
                int(string)
                return True
            except ValueError:
                return False
        stack = []
        for op in operations:
            if isInteger(op):
                print(op)
                stack.append(int(op))
            elif op=='+':
                stack.append(stack[-1]+stack[-2])
            elif op=='D':
                # print(stack)
                stack.append(2*stack[-1])
            elif op=='C':
                stack.pop()
        sum=0
        # print(stack)
        for num in stack:
            sum+=num
        return sum