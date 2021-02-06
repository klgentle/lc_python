"""
99. Recover Binary Search Tree
Hard

You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

 

Example 1:

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

"""


class Solution:
    def __init__(self):
        self.val_list = []
    
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # 先中序遍历一下，找到需要更改的位置，然后再来一遍，修改数据
        self.tree2List(root)
        right_val = sorted(self.val_list)
        #print(f"right_val:{right_val}")
        root = self.correctTree(root, right_val)
        
    def tree2List(self, root):
        if not root:
            return
        
        self.tree2List(root.left)
        self.val_list.append(root.val)
        self.tree2List(root.right)
        
    def correctTree(self, root, right_val:list):
        if not root:
            return
        
        self.correctTree(root.left, right_val)
        val = right_val.pop(0)
        
        if root.val != val:
            root.val = val
        self.correctTree(root.right, right_val)
        
        return root
