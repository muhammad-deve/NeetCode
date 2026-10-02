# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        result = 0

        def DFS(current) -> int:
            if not root:
                return 0

            nonlocal result
            left_hight = self.maxDepth(root.left)
            right_hight = self.maxDepth(root.right)

            current_hight = 1 + max(left_hight, right_hight)
            result = max(result, current_hight)

            return current_hight

        DFS(root)
        return result
        
