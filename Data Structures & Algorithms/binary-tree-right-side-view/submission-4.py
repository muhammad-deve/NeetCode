# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We can do Level Order Traversel and get the second elemnt of the ARRAY
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        array, result = [], []

        while len(queue) != 0:
            level = []
            for _ in range(len(queue)):
                current = queue.popleft()
                level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            array.append(level)
        
        # array = [[1], [2, 3], [4, 5]] ===> [1, 3, 5]
        for arr in array:
            if len(arr) == 1:
                result.append(arr[0])
            else:
                result.append(arr[-1])
        
        return result

            