"""
101. Symmetric Tree
Easy

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Follow up: Solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        treelist = []
        def tree2list(root: TreeNode) -> list:
            # 中序遍历（左根右） 
            if not root:
                treelist.append(-1)
                return
            
            tree2list(root.left)
            treelist.append(root.val)
            tree2list(root.right)
            
            return treelist
        
        treelist = tree2list(root)
        print(f"treelist:{treelist}")
        
        r = root
        l = root
        straight_left = []
        straight_right = []
        while r.right:
            straight_left.append(r.right.val)
            r = r.right
        while l.left:
            straight_right.append(l.left.val)
            l = l.left            
        
        return treelist == treelist[::-1] and straight_left == straight_right
