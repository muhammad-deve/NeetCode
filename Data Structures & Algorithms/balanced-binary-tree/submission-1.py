# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = [True]

        # This calculates the HIGHTS!
        def DFS(current):
            if not current:
                return 0
            
            left_hight = DFS(current.left)
            right_hight = DFS(current.right)

            if abs(left_hight - right_hight) > 1:
                result[0] = False
            
            # Formula of HIGHT: 1 + max(left, right)
            return 1 + max(left_hight, right_hight)
        
        DFS(root)

        return result[0]
