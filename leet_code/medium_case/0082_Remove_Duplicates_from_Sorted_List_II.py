# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates0(self, head: ListNode) -> ListNode:
        """find duplicate value, and add this value in duplicate set
           if node.val in duplicate set then skip this node
        """
        value_set = set()
        dupl_set = set()
        node = head        
        while node:
            if node.val not in value_set:
                value_set.add(node.val)
            else:
                dupl_set.add(node.val)
            node = node.next
        
        dummy = ListNode(None)
        dummy.next = head
        node = dummy
        while node.next:
            if node.next.val in dupl_set:
                # skip node
                node.next = node.next.next
            else:
                node = node.next
                        
        return dummy.next
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """ construct a dummy list node: dummy, the head is pre, value is 0.
            find the distinct element, and let pre point to it
            at last return the node list except head (pre)
        """
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head  ### core is here
            else:
                pre = pre.next
                head = head.next
        return dummy.next
