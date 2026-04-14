class Solution:
    """
    Three cases:
    a is positive and top is negative
    a is negative and top is positive
    both are equal


    one num is positive one is negative and they are greater>= to each other
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        def canEnterWhile(a: int, top: int):
            if a>0 and top<0 or a<0 and top>0:
                # print(a, top)
                return True
            else:
                return False

        for a in asteroids:
            destroyed=False
            while stack and a<0 and stack[-1]>0 and not destroyed:
                if abs(a) == abs(stack[-1]):
                    stack.pop()
                    destroyed=True
                elif abs(a) > abs(stack[-1]):
                    stack.pop()
                else:
                    destroyed=True
                    break

            if not destroyed:
                # print("appending", a)
                stack.append(a)
        return stack

