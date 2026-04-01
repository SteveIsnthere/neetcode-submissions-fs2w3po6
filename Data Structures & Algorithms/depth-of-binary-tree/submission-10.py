# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = [[root,1]]
        v = 1
        while len(q)>0:
            c = q.pop()
            if c[0].right:
                q.append([c[0].right,c[1]+1])
                if c[1]+1 > v: v = c[1]+1
            if c[0].left:    
                q.append([c[0].left,c[1]+1])
                if c[1]+1 > v: v = c[1]+1
        return v