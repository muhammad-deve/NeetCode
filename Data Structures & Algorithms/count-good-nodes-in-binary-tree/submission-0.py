# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        
        def DFS(current, max_so_far):
            if not current:
                return 0
            
            nonlocal result
            if current.val >= max_so_far:
                result += 1

            new_max = max(max_so_far, current.val)

            DFS(current.left, new_max)
            DFS(current.right, new_max)

        DFS(root, -inf)
        return result

