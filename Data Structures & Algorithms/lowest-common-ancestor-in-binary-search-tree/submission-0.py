# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        qu = deque([root])

        lv = p.val
        sv = q.val

        if lv < sv:
            t = lv
            lv = sv
            sv = t

        while len(qu)>0:
            c = qu.popleft()
            if c.val <= lv and c.val >= sv:
                return c

            if c.left: qu.append(c.left)
            if c.right: qu.append(c.right)
        return root

