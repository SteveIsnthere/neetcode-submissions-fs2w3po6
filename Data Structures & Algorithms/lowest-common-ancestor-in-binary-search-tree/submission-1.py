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

        c = root

        while c:
            if c.val > lv:
                c = c.left
                continue
            if c.val < sv:
                c = c.right
                continue
            return c
        return root

