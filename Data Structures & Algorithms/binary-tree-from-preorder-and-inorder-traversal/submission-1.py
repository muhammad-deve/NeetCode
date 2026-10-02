# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # value -> its position in inorder
        inorder_pos = {}
        for i in range(len(inorder)):
            inorder_pos[inorder[i]] = i

        pre_index = 0

        # Builds the subtree whose values are inorder[left..right]
        def DFS(left, right):
            nonlocal pre_index

            if left > right:
                return None

            root_val = preorder[pre_index]
            pre_index += 1
            root = TreeNode(root_val)

            mid = inorder_pos[root_val]

            root.left = DFS(left, mid - 1)
            root.right = DFS(mid + 1, right)

            return root

        return DFS(0, len(inorder) - 1)