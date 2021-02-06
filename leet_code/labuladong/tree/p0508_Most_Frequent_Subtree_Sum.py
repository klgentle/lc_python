"""
508. Most Frequent Subtree Sum
Medium

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3

return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5

return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def dfs(root):
            if not root:
                return 0

            s = root.val + dfs(root.left) + dfs(root.right)
            if s not in count:
                count[s] = 1
            else:
                count[s] += 1
            return s

        count = {}
        dfs(root)
        max_value = max(count.values())

        return [s for s in count if count[s] == max_value]
