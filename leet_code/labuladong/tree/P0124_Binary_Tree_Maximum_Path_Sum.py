"""
124. Binary Tree Maximum Path Sum
Hard

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = -99999999999999999

    def onePathSum(self, root):
        # root.left == None 无效
        if root is None:
            return 0
        left = max(0, self.onePathSum(root.left))
        right = max(0, self.onePathSum(root.right))
        self.ans = max(self.ans, left + right + root.val)
        return max(left, right) + root.val  # 为什么是max(left, right) 因为是求max,不是求和

    def maxPathSum(self, root: TreeNode) -> int:
        self.onePathSum(root)
        return self.ans
