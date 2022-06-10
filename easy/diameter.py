# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calculate(root):
            if root is None:
                return -1
            lh = calculate(root.left)
            rh = calculate(root.right)
            self.diameter = max(self.diameter,lh+rh+2)
            return max(lh,rh) + 1
        calculate(root)
        return self.diameter