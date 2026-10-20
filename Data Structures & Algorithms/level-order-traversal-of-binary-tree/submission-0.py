# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        layers = {root: 0}
        q = deque([root])
        ans = [[root.val]]

        while q:

            node = q.popleft()
            left = node.left
            right = node.right

            if left or right:
                level = layers[node] + 1
                if level > len(ans) - 1:
                    ans.append([])

            if left and left not in layers:
                layers[left] = level 
                ans[level].append(left.val)
                q.append(left)

            if right and right not in layers:
                layers[right] = level 
                ans[level].append(right.val)
                q.append(right)

        return ans
        
