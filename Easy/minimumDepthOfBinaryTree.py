# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    steps = []
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs_depth(root):
            if root is None:
                return 0
            #Recursively traversing the tree
            left = dfs_depth(root.left)    
            right = dfs_depth(root.right)
            
            #Condtion for a leaf node. On encountering a leaf node to grt the number of sub nodes in 
            #sub tree
            if left==0 or right==0:
                return (1+max(left,right))
            #Else the minimum path from calling node to the leaf node must be returned
            return(1+min(left,right))
            
        return dfs_depth(root)
            
