# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums is None:
            return None
    
        def findMid(nums, l, r):
            if l>=r:
                return None
            
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            #First the left subtree is populated with elements to the left of mid element(head node)
            #The right subtree is populated after, followed by the appropriate number of left subtrees
            #The tree will be height balanced since a binary serach approach is being used
            node.left = findMid(nums,l,mid)
            node.right = findMid(nums,mid+1,r)
                
            return node
        
        return findMid(nums, 0, len(nums))
