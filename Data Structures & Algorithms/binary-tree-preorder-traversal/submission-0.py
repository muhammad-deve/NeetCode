# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive version
        result = []

        def DFS(current):
            if not current:
                return []

            result.append(current.val)

            if current.left:
                DFS(current.left)
            
            if current.right:
                DFS(current.right)
        
        DFS(root)

        return result

