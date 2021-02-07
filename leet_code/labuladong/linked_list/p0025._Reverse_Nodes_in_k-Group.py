"""
25. Reverse Nodes in k-Group
Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

    Could you solve the problem in O(1) extra memory space?
    You may not alter the values in the list's nodes, only nodes itself may be changed.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return

        a, b = head, head
        for i in range(0,k):
            # base case
            if not b:
                return head
            b = b.next

        newhead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newhead


    def reverse(self, a: ListNode, b: ListNode) -> ListNode:
        pre = None
        while a != b:
            curr = a
            # 往下走一个
            a = a.next
            curr.next = pre
            pre = curr

        return pre
