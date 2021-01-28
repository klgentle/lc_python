"""
Given the root of a binary tree, flatten the tree into a "linked list":

    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return

        # 拉平左右子树
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left  # flatten 没有返回值，不能用函数赋值
        right = root.right

        # 把链表挂在右边
        root.left = None
        root.right = left

        # 把右链表挂在右子树
        point = root
        while point.right is not None:
            point = point.right

        point.right = right
