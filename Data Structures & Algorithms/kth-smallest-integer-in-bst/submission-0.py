# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 0
        
        i = 0
        res = 0
        def dfs(n):
            nonlocal i
            nonlocal res
            if not n: return
            dfs(n.left)
            i = i + 1
            if i == k: res = n.val
            dfs(n.right)

        dfs(root)

        return res

        