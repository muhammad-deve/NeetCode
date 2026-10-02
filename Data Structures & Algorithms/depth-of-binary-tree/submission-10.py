# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative BFS
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        result, level = 0, 0

        while len(queue) != 0:
            for _ in range(len(queue)):
                current = queue.popleft()

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            level += 1
            result = max(result, level)
        
        return result







