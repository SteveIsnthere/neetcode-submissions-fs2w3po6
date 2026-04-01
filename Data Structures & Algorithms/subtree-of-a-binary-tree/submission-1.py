# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        def is_matching_head(r):
            if not r: return False
            return r.val == subRoot.val

        def attemp_search(head):
            q_r = deque([head])
            q_s = deque([subRoot])

            while len(q_s) > 0:
                if len(q_r) == 0: return False
                c_r = q_r.popleft()
                c_s = q_s.popleft()

                if c_r.val != c_s.val: return False

                if c_r.left: 
                    if c_s.left: 
                        q_s.append(c_s.left)
                    else:
                        return False
                    q_r.append(c_r.left)
                if c_r.right: 
                    if c_s.right: 
                        q_s.append(c_s.right)
                    else:
                        return False
                    q_r.append(c_r.right)

                if c_s.left and not c_r.left:
                    return False
                if c_s.right and not c_r.right:
                    return False
                
            return True

        q = deque([root])


        while len(q)>0:
            c = q.popleft()
            if is_matching_head(c):
                if attemp_search(c):
                    return True
        
            if c.left: q.append(c.left)
            if c.right: q.append(c.right)
        
        return False