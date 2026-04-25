class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, minn, maxx):
            if not node:
                return True
            if node.val<=minn or node.val>=maxx:
                return False
            return traverse(node.left, minn, node.val) and traverse(node.right, node.val, maxx)
        return traverse(root, float('-inf'), float('inf'))