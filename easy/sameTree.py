# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self,root,res):
        if root is None:
            res.append(None)
        elif root is not None:
            res.append(root.val)
            self.inOrder(root.left,res)
            self.inOrder(root.right,res)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = []
        self.inOrder(p,res1)
        res2 = []
        self.inOrder(q,res2)
        return res1==res2