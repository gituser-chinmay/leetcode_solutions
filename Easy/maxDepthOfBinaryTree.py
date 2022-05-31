# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        #The recursive function traverses to the end node of each sub tree and sets values of left and right as 0 starting
        #from there. For parent nodes, the max(left,right)+1 gives the number of left and right nodes it contains
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
  
        return max(left,right)+1
        
        
