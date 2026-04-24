from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or q.val!= p.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)


        # def bst(root):
        #     arr = []
        #     q = deque()
        #     q.append(root)
        #     while len(q)>0:
        #         for i in range(len(q)):
        #             node = q.popleft()
        #             if not node:
        #                 arr.append(None)
        #                 continue
        #             arr.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     return arr

        # arrP = bst(p)
        # arrQ = bst(q)
        # print(arrP, arrQ)
        # return arrP == arrQ
        
                

            