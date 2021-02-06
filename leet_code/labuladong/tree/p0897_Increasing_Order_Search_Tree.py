"""
897. Increasing Order Search Tree
Easy

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:

Input: root = [5,1,7]
Output: [1,null,5,null,7]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # get value in list
        # constract tree from list
        
        vl = []
        def getValueList(root):
            if not root:
                return
            
            getValueList(root.left)
            vl.append(root.val)
            
            getValueList(root.right)
            return vl
        
        def constractTree(vl) -> TreeNode:
            if not vl:
                return 
            
            root = TreeNode(vl.pop(0))        
            root.right = constractTree(vl)
            
            return root           
        
        vl = getValueList(root)
        #print(f"vl:{vl}")
        
        return constractTree(vl)
        
