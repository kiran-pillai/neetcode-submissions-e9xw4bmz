class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands={'+':True, '-':True, '*':True, '/':True}
        stack=[]
        res=None
        def handleOperation(operator, num, num2) -> int:
            if operator=='+':
                return num2 + num
            elif operator == '-':
                return num2 - num
            elif operator == '*':
                return num2 * num
            elif operator =='/':
                return float(int(num2 / num))

        for token in tokens:
            is_operator=operands.get(token)
            if not is_operator:
                stack.append(token)
            if is_operator:
                num1=stack.pop()
                num2=stack.pop()
                stack.append(handleOperation(token, int(num1), int(num2)))
        return int(stack[0])






