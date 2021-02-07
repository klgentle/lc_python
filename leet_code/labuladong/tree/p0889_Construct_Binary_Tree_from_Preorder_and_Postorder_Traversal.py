"""
889. Construct Binary Tree from Preorder and Postorder Traversal
Medium

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

 

Note:

    1 <= pre.length == post.length <= 30
    pre[] and post[] are both permutations of 1, 2, ..., pre.length.
    It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.


"""

class Solution:
    """
    A preorder traversal is:
        (root node) (preorder of left branch) (preorder of right branch)
    While a postorder traversal is:
        (postorder of left branch) (postorder of right branch) (root node)
    """
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None

        root = TreeNode(pre[0])
        # 防止返回多余的空结点
        if len(pre) == 1:
            return root

        # 根据左子树的根结点确定左边子树结点树，然后分左右
        len_of_left = post.index(pre[1]) + 1
        # root, left, right
        root.left = self.constructFromPrePost(pre[1:len_of_left+1], post[:len_of_left])
        root.right = self.constructFromPrePost(pre[len_of_left+1:], post[len_of_left:-1])

        return root
