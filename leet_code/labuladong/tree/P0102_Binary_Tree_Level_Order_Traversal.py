"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
"""

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        q, result = deque(), []
        if root:
            q.append(root)

        while q:
            level = []

            for _ in range(len(q)):
                x = q.popleft()
                level.append(x.val)

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

            result.append(level)

        return result
