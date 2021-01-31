"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example 1:

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
"""

class Solution:
    def __init__(self):
        self.memo = {}
        self.res = []
    
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.TreeNodeSerialization(root)
        return self.res        
        
    def TreeNodeSerialization(self, root: TreeNode):
        if not root:
            return "#"
        
        left = self.TreeNodeSerialization(root.left)
        right = self.TreeNodeSerialization(root.right)        
        subTree = f"{left},{right},{root.val}"
        
        if subTree in self.memo:
            self.memo[subTree] += 1
            # 无法用in list判断root是不是已经在self.res中，毕竟这个结构比较复杂
            if self.memo[subTree] == 2:
                self.res.append(root)
        else:
            self.memo[subTree] = 1
        
        return subTree
