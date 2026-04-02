# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lv = p.val
        sv = q.val

        if lv < sv:
            t = lv
            lv = sv
            sv = t

        def search(n):
            if n.val > lv:
                return search(n.left)
            if n.val < sv:
                return search(n.right)
            return n
        
        return search(root)

