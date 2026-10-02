# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        # It retruns HIGHT of the NODE
        def DFS(current):
            if not current:
                return 0
            
            nonlocal diameter
            left_hight = DFS(current.left)
            right_hight = DFS(current.right)

            diameter = max(diameter, left_hight + right_hight)
            current_hight = 1 + max(left_hight, right_hight)

            return current_hight
        
        DFS(root)
        return diameter