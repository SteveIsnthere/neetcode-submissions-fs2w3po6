# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        c_l = deque([root])
        n_l = deque([])

        r = []
        _r = []

        while len(c_l)>0:
            c = c_l.popleft()
            _r.append(c.val)

            if c.left: n_l.append(c.left)
            if c.right: n_l.append(c.right)

            if len(c_l) == 0:
                c_l = n_l
                n_l = deque()
                r.append(_r)
                _r = []

        return r