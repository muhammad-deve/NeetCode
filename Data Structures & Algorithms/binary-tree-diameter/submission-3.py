# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        diameter = 0

        # Retunrs HIGH of the NODE
        def HightTree(current):
            if not current:
                return 0
            
            nonlocal diameter
            left_hight = HightTree(current.left)
            right_hight = HightTree(current.right)
            
            current_hight = 1 + max(left_hight, right_hight)
            diameter = max(diameter, left_hight + right_hight)

            return current_hight
        
        HightTree(root)

        return diameter
