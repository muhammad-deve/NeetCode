# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True

        # Returns HIGHT of the NODE
        def DFS(current):
            if not current:
                return 0
            
            nonlocal result
            left_hight = DFS(current.left)
            right_hight = DFS(current.right)

            if abs(left_hight - right_hight) > 1:
                result = False

            current_hight = 1 + max(left_hight, right_hight)

            return current_hight
        
        DFS(root)
    
        return result