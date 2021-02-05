"""
92. Reverse Linked List II
Medium

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.successor = ListNode()

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if m ==1:
            return self.reverseN(head, n)
        # 指针往前移
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

    def reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            self.successor = head.next
            return head

        # 递归反转
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor

        return last
