# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        ntv = [root]
        while ntv:
            n = ntv[0]

            t = n.left
            n.left = n.right
            n.right = t
            if n.left:
                ntv.append(n.left)
            if n.right:
                ntv.append(n.right)
            ntv.pop(0)

        return root


        