# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        
        def DFS(current):
            if not current:
                return
            
            DFS(current.left)
            result.append(current.val)
            DFS(current.right)
        
        DFS(root)

        print(result)
        return result == sorted(set(result))