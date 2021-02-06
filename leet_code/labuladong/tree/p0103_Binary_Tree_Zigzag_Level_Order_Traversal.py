"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
"""

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q, result = deque(), []
        redirect = False

        if root:
            q.append(root)

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            # print(f"redirect:{redirect}, level:{level}")
            # 调整加入顺序
            if redirect:
                level.reverse()
            result.append(level)
            # change redirect
            redirect = not redirect

        return result
