# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invertChildren(node):
            node.left, node.right = node.right, node.left
            return node
        if root is not None:
            children = [root]
        else:
            return None
        while len(children) != 0:
            for child in children:
                invertChildren(child)
                children.remove(child)
                if child.left is not None:
                    children.append(child.left)
                if child.right is not None:
                    children.append(child.right)
        return root
        