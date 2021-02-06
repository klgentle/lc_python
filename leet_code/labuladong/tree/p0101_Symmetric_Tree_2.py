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



class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        # 每一层结点，应该是对称的
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            
            for _ in range(len(q)):
                x = q.popleft()
                
                if not x:
                    level.append(-1)
                else:
                    level.append(x.val)
                    q.append(x.left)
                    q.append(x.right)
                    
            #print(f"level:{level}")
            if level != level[::-1]:
                return False
            
        return True
