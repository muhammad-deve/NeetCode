# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = [True]

        def DFS(current) -> int:
            if not current:
                return 0
            
            left_branch = DFS(current.left)
            right_branch = DFS(current.right)

            if abs(left_branch - right_branch) > 1:
                result[0] = False

            current_branch = 1 + max(left_branch, right_branch)
            return current_branch
            
        DFS(root)
        return result[0]
