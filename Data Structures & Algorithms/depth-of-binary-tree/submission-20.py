# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS: Level Order Traversel
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)
        result = 0

        while len(queue) != 0:
            for _ in range (len(queue)):
                current = queue.popleft()
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                
            result += 1
        
        return result









        