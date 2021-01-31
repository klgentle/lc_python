"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

"""

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        
        return f"{root.val},{left},{right}"
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        return self.deserializeIteration(nodes)
    
    def deserializeIteration(self, nodes):
        if not nodes:
            return None
        
        #print(f"nodes:{nodes}")
        root_val = nodes.pop(0)
        if root_val == "#":
            return None
        
        root = TreeNode(root_val)
        # 无法区分左右，直接交给递归. 递归会不断减少数据，left全部减少之后就只剩right
        root.left = self.deserializeIteration(nodes)
        root.right = self.deserializeIteration(nodes)
        
        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
