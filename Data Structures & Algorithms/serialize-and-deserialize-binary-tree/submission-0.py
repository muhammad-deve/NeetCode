# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Pre Order Traversel
        result = []

        def DFS(current):
            if not current:
                result.append("N")
                return
            
            result.append(str(current.val))
            
            DFS(current.left)
            DFS(current.right)
        
        DFS(root)
        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # ['1', '2', 'N', 'N', '3', '4', 'N', 'N', '5', 'N', 'N']
        preorder = data.split(",")
        i = 0
        
        def DFS():
            nonlocal i

            if preorder[i] == "N":
                i += 1
                return None
            
            node = TreeNode(int(preorder[i]))
            i += 1

            node.left = DFS()
            node.right = DFS()

            return node
        
        return DFS()





























