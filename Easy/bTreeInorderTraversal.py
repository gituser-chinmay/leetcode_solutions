# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #If the root is empty, return null
        if not root:
            return
        
        res = []
        #A recursive function to populate the res array. The function recursively travels to
        #the leftmost node and appends the value to res
        def recursive(node):
            #This is the case for the last element in inorder traversal, that is the rightmost node
            #The value of node is appended an function breaks
            if not node.left and not node.right:
                res.append(node.val)
                return
            if node.left:
                recursive(node.left)
            #if node.left is none, the function has reached the leftmost node and the value is appended
            res.append(node.val)
            #Then it recursively travels to the rightmost node, then repeats process of checking for a left sub-node
            if node.right:
                recursive(node.right)
                
        recursive(root)
        
        return res
