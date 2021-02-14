"""
199. Binary Tree Right Side View
Medium

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""

from collections import deque


class Solution:
    """
    此解法的模板可以解决很多个题目，只要是分层查看就可以使用
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        q = deque()
        
        if root:
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
        
            ans.append(level[-1])
            
        return ans

