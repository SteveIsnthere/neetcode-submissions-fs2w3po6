# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        nodes_to_visit = [root]
        while len(nodes_to_visit) > 0:
            c = nodes_to_visit.pop()
            t = c.left
            c.left = c.right
            c.right = t
            if c.right: nodes_to_visit.append(c.right)
            if c.left: nodes_to_visit.append(c.left)

        return root