# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return False
        
    def sameTree(self, s, t) -> bool:
        if not s and not t:
            return True
        
        if (s and not t) or (not s and t):
            return False
        
        if s.val != t.val:
            return False
        
        left_branch = self.sameTree(s.left, t.left)
        right_branch = self.sameTree(s.right, t.right)

        return left_branch and right_branch