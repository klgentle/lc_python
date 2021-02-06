"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not inorder:
            return

        root_value = preorder.pop(0)
        root = TreeNode(root_value)
        root_index = inorder.index(root_value)

        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1 :])

        return root
