/*
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
*/

class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);        
        int depth = 1;
        
        while (!q.isEmpty()) {
            int sz = q.size();
            for (int i = 0; i< sz; i++) {
                TreeNode cur = q.poll();
                
                if (cur.left == null && cur.right == null) 
                    return depth;
                if (cur.left != null) 
                    q.offer(cur.left);
                if (cur.right != null)
                    q.offer(cur.right);
            }
            depth += 1;
        }
        return depth;
    }
}
