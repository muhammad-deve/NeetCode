# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # InOrder Traversel
        array = []

        def DFS(current):
            if not current:
                return 
            
            DFS(current.left)
            array.append(current.val)
            DFS(current.right)
        
        DFS(root)
        return array[k - 1]
