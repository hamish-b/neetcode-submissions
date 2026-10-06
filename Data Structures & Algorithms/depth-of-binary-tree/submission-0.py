# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0

        q = deque([root])
        depth = {root : 1}
        max_depth = 1

        while q:
            node = q.popleft()

            for child in [node.left, node.right]:
                if child is not None and child not in depth:
                    a = depth[node] + 1
                    depth[child] = a
                    q.append(child)
                    if a > max_depth:
                        max_depth = a
        return max_depth
