# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #A class variable is used to hold the return value
    ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            self.ans = True
        def dfs_height(root):
            if not root:
                return 0
            #The function recursively traverses the tree starting from the left subtree,
            #then checks the right subtrees of the sub-nodes
            left = dfs_height(root.left)
            right = dfs_height(root.right)
            
            #Condtion for height balanced tree
            if abs(left-right)>1:
                self.ans=False
            
            #This returns the number of nodes of a subtree, max is used because a node can have both 
            #sub trees or a sub-tree on only one of either side
            return 1+max(left,right)
        
        dfs_height(root)
        return self.ans
