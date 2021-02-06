"""
450. Delete Node in a BST
Medium

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.

Follow up: Can you solve it with time complexity O(height of tree)?

Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return

        if key == root.val:
            """
            三种情况：
                1 只有根结点，直接返回；
                2 只有一个子结点，返回子结点；
                3 有两个子结点，为了不破坏结构，需要找到左子树最大结点，或者右子树最小结点替换根结点
            """
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if root.left and root.right:
                root.val = self.minVal(root.right)
                # print(f"root.val:{root.val}")
                root.right = self.deleteNode(root.right, root.val)

        elif key < root.val:
            # 更新左结点
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        return root

    def minVal(self, root: TreeNode) -> int:
        while root.left:
            root = root.left
        return root.val
