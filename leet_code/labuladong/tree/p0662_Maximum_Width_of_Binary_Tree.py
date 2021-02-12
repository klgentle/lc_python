"""
662. Maximum Width of Binary Tree
Medium

Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

"""

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        
        for node, depth, pos in queue:
            #print(f"depth:{depth}")
            if node:
                # set position of left is 2 * (root position), rigth is 2 * pos +1
                queue.append((node.left, depth+1, pos * 2))
                queue.append((node.right, depth+1, pos * 2 +1))
                
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                # R - L + 1 = length of level
                ans = max(ans, pos - left +1)
            
        return ans
