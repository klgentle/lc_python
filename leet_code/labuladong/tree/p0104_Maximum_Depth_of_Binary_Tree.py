"""
104. Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Example 3:

Input: root = []
Output: 0

Example 4:

Input: root = [0]
Output: 1
"""


class Solution:
    
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = 0
        q = collections.deque()
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
                
            depth += 1
            
        return depth
