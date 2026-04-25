from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def bst(root):
            traversal = []
            q = deque()
            q.append(root)
            while len(q)>0:
                level_order = []
                for _ in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    level_order.append(node.val)
                traversal.append(level_order)
            return traversal
        return bst(root)
                    

                    
               