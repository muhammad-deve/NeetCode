# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
    
        # Returns the HIGHT of the NODE
        def DFS(current) -> int:
            if not current:
                return 0
            
            left_hight = DFS(current.left)
            right_hight = DFS(current.right)
            nonlocal result

            current_hight = 1 + max(left_hight, right_hight)
            result = max(result, left_hight + right_hight)
            
            return current_hight
        
        DFS(root)
        return result