# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}

        def dfs(n,d):
            if not n: return
            if d in res.keys():
                res[d].append(n.val)
            else:
                res[d] = [n.val]
            dfs(n.left, d+1)
            dfs(n.right, d+1)

        dfs(root,1)

        r = []
        ks = list(res.keys())
        ks.sort()
        for k in ks:
            r.append(res[k])
        
        return r