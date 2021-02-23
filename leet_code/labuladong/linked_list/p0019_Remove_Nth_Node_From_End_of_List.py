"""
19. Remove Nth Node From End of List
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

 

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        fast 先走 n 步，slow再走，fast到达尾部时，slow就到达倒数 n 个
        """
        fast = head
        slow = head

        while n > 0:
            fast = fast.next
            n -= 1

        if not fast:
            # 倒数第 n 个是 head
            return head.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        # delete node
        slow.next = slow.next.next

        return head
