# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        head = dummy

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            if total >= 10:
                carry = 1
            else:
                carry = 0
            node_val = total % 10
            node = ListNode(node_val)
            head.next = node
            head = head.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            head.next = ListNode(carry)
        
        return dummy.next
