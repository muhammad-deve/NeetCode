# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative traversial
        if not root:
            return []

        stack = [root]
        result = []
        
        while len(stack) != 0:
            current = stack.pop()
            result.append(current.val)

            if current.right:
                stack.append(current.right)
            
            if current.left:
                stack.append(current.left)
            
        
        return result
