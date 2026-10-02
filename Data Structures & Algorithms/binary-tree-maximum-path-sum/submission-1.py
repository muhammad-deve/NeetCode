# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        # Retruns SUM PATH
        def DFS(current):
            if not current:
                return 0
            
            nonlocal result
            left_path = DFS(current.left)
            right_path = DFS(current.right)
            left_path = max(left_path, 0)
            right_path = max(right_path, 0)

            current_path = current.val + left_path + right_path
            result = max(result, current_path)

            return current.val + max(left_path, right_path)

        DFS(root)
        return result