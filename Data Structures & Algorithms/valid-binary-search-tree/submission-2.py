# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # PreOrder Traversel gives SORTED List if it is BST
        array = []
        def DFS(current):
            if not current:
                return None
            
            DFS(current.left)
            array.append(current.val)
            DFS(current.right)
        
        DFS(root)
        return array == sorted(set(array))
