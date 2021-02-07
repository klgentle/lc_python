"""
112. Path Sum
Easy

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:

Input: root = [1,2], targetSum = 0
Output: false

"""
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            if targetSum == root.val:
                return True
            return False
        
        targetSum = targetSum - root.val
        
        left_has = False
        right_has = False
        if root.left:
            left_has = self.hasPathSum(root.left, targetSum)
        if root.right:
            right_has = self.hasPathSum(root.right, targetSum)
        
        return left_has or right_has
