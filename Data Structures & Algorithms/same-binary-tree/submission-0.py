# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not (p and q): return False
        if p.val != q.val: return False

        q1 = deque([p])
        q2 = deque([q])
        while len(q1) > 0:
            c1 = q1.pop()
            c2 = q2.pop()
            
            if not (not c1.left and not c2.left):
                if not (c1.left and c2.left): return False
                if c1.left.val != c2.left.val: return False
                q1.appendleft(c1.left)
                q2.appendleft(c2.left)

            if not (not c1.right and not c2.right):
                if not (c1.right and c2.right): return False
                if c1.right.val != c2.right.val: return False
                q1.appendleft(c1.right)
                q2.appendleft(c2.right)

        return True