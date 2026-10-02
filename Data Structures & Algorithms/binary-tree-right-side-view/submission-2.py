# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        result = []

        while len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                current = queue.popleft()
                level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            result.append(level)
        
        # [[1], [2, 3], [4, 5]] ===> [1, 3, 5]
        actual_result = []

        for array in result:
            if len(array) == 1:
                actual_result.append(array[0])
            else:
                actual_result.append(array[-1])
        
        return actual_result













