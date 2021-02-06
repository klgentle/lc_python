"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

 

Example 1:

Input: root = [2,1,3]
Output: true

"""


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTSub(root, -2 ** 32, 2 ** 32 - 1)

    def isValidBSTSub(self, root, minVal, maxVal) -> bool:

        # 大树化成左右子树

        if not root:
            return True

        if root.val <= minVal or root.val >= maxVal:
            return False

        return self.isValidBSTSub(root.left, minVal, root.val) and self.isValidBSTSub(
            root.right, root.val, maxVal
        )
