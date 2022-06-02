# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, current_sum):
            #Base Condition
            if root is None:
                return False
            
            current_sum+=root.val
            #Condtion for leaf node
            if not root.left and not root.right and current_sum==targetSum:
                return True
            #Recursive call for traversing tree. If a oath exists to a leaf in either sub tree from the root,
            #such that the sum of values is equal to target sum, then function wil return true
            if dfs(root.left,current_sum) or dfs(root.right,current_sum):
                return True
        return dfs(root,0)
