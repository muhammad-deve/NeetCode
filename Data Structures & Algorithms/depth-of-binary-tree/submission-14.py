# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS
        if not root:
            return 0
        
        stack = [[root, 1]]
        result = 0

        while len(stack) != 0:
            current, depth = stack.pop()
            result = max(result, depth)

            if current.right:
                stack.append([current.right, depth + 1])
            if current.left:
                stack.append([current.left, depth + 1])
        
        return result
            
        