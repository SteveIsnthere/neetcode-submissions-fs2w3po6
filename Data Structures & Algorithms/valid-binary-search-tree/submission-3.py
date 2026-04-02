# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        flat = []

        def dsf(n):
            if not n: return
            dsf(n.left)
            flat.append(n.val)
            dsf(n.right)

        dsf(root)
        
        last = flat[0] - 1 
        for n in flat:
            if n>last:
                last = n
                continue
            return False

        return True
