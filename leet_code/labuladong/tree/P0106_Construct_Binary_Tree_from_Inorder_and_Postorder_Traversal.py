"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val) # Line A

        # 为什么先计算右边的就可以出来？先左边的就不行
        # 因为右结点离根结点近(就是因为左右顺序搞错，浪费了一下午时间)
        root.right = self.buildTree(inorder[inorderIndex+1:], postorder) # Line B
        root.left = self.buildTree(inorder[:inorderIndex], postorder) # Line C

        return root
