# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        # Returns the HIGHT
        def dfs(current):
            if not current:
                return 0
            
            nonlocal result
            
            left = dfs(current.left)
            right = dfs(current.right)

            result = max(result, left + right)
            
            return max(left, right) + 1
        
        dfs(root)

        return result

