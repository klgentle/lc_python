"""
437. Path Sum III
Medium

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""

class Solution:
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.result = 0
        cache = {0:1} # 0:1 什么时候用？ currPathSum = target
    
        self.dfs(root, sum, 0, cache)
        return self.result
    
    
    def dfs(self, root, target, currPathSum, cache):
        if not root:
            return
        
        currPathSum += root.val
        oldPathSum = currPathSum - target
        
        # oldPathSum exists 则加
        self.result += cache.get(oldPathSum, 0)
        
        # 每个节点计算一次
        cache[currPathSum] = cache.get(currPathSum, 0) +1
        print(f"cache:{cache}")
        
        
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1
