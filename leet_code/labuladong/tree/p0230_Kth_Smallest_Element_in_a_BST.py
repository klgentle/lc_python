"""
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

"""

class Solution:
    def __init__(self):
        self.treeList = []

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.constructList(root, k)
        return self.treeList[k-1]

    def constructList(self, root, k):
        if not root:
            return

        #print(self.treeList)
        # 跳过不需要的部分
        if len(self.treeList) >= k:
            return self.treeList

        self.constructList(root.left, k)
        self.treeList.append(root.val)
        self.constructList(root.right, k)
