"""
382. Linked List Random Node
Medium

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

 

Example 1:

Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]
"""

from random import randint
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self._head = head


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        第 i 个元素被选择的概率是 1/i，第 i+1 次不被替换的概率是 1 - 1/(i+1)，以此类推，
        相乘就是第 i 个元素最终被选中的概率，就是 1/n。
        """
        result, node, index = self._head, self._head.next, 1
        while node:
            if randint(0, index) == 0:
                result = node
            index += 1
            node = node.next
        return result.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
