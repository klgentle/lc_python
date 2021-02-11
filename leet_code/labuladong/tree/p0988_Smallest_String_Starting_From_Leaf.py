"""
988. Smallest String Starting From Leaf
Medium

Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)

 

Example 1:

Input: [0,1,2,3,4,3,4]
Output: "dba"

Example 2:

Input: [25,1,3,1,3,0,2]
Output: "adz"

"""

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.res = []
        
        self.dfs(root, [])
        self.res.sort()
        #print(f"self.res:{self.res}")
        return self.res[0]
    
    def dfs(self, root, ls=[]):
        if root:
            if not root.left and not root.right:
                ls.append(root.val)
                # chr(97) = 'a'
                s = [chr(97+i) for i in ls[::-1]]
                self.res.append("".join(s))            
            
            self.dfs(root.left, ls+[root.val])
            self.dfs(root.right, ls+[root.val])
