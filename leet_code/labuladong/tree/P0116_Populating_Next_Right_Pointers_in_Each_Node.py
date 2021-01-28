"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from typing import List, Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        self.connectTwoNode(root.left, root.right)
        return root

    def connectTwoNode(self, node1: 'None', node2: 'None'):
        if node1 is None or node2 is None:
            return None

        # 连接顶点
        node1.next = node2

        self.connectTwoNode(node1.left, node1.right)
        self.connectTwoNode(node2.left, node2.right)
        self.connectTwoNode(node1.right, node2.left)


if __name__ == "__main__":
    a = Solution()
    root = [1,2,3,4,5,6,7] 
    print(a.connect(root))

