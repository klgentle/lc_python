"""
113. Path Sum II
Medium

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

 

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:

Input: root = [1,2], targetSum = 0
Output: []

"""

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root: TreeNode, targetSum: int, ls, res):
        if root:
            if not root.left and not root.right and root.val == targetSum:
                ls.append(root.val)
                res.append(ls)

            # 将列表直接在参数中运算，左右就可以独立不受影响
            self.dfs(root.left, targetSum-root.val, ls+[root.val], res)
            self.dfs(root.right, targetSum-root.val, ls+[root.val], res)
