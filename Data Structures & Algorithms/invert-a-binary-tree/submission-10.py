# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative BFS
        if not root:
            return None
        
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            current = queue.popleft()

            current.left, current.right = current.right, current.left
            
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        
        return root