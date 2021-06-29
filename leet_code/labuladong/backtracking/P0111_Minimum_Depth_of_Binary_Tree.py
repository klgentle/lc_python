"""
111. Minimum Depth of Binary Tree
Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if (not root): return 0;
        q = list()
        q.append(root);
        depth = 1

        while (q):
            sz = len(q);
            for i in range(sz):
                cur = q.pop(0);

                if (not cur.left and not cur.right):
                    return depth
                if (cur.left):
                    q.append(cur.left);
                if (cur.right):
                    q.append(cur.right);
            depth += 1
        return depth
