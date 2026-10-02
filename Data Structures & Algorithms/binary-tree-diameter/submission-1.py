# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        result = 0

        # Helper function to calculate the HIGHT of the NODE
        def DFS(current):
            if not current:
                return 0
            
            nonlocal result
            
            left_hight = DFS(current.left)
            right_hight = DFS(current.right)
            
            current_hight = 1 + max(right_hight, left_hight)
            result = max(result, left_hight + right_hight)

            return current_hight
        
        DFS(root)

        return result

            
