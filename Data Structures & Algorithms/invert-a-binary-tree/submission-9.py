# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        def r(node: Optional[TreeNode]):
            if not node: return node
            node.left, node.right = node.right, node.left
            r(node.left)
            r(node.right)

        r(root)
        return root