# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        def dfs(node):
            nonlocal counter
            nonlocal k
            if not node:
                return
            node_left = dfs(node.left)
            if node_left:
                return node_left
            counter+=1
            if counter == k:
                return node.val
            node_right = dfs(node.right)
            if node_right:
                return node_right
        return dfs(root)