# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carryOver = 0
        while l1 and l2:
            total = l1.val + l2.val + carryOver
            if total >= 10:
                carryOver = 1
            else:
                carryOver = 0
            curr.next = ListNode(total % 10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
            
        
        while l1:
            total = l1.val + carryOver
            if total >= 10:
                carryOver = 1
            else:
                carryOver = 0
            curr.next = ListNode(total % 10)
            curr = curr.next
            l1 = l1.next
        while l2:
            total = l2.val + carryOver
            if total >= 10:             
                carryOver = 1
            else:
                carryOver = 0
            curr.next = ListNode(total % 10)
            curr = curr.next
            l2 = l2.next
        
        if carryOver == 1:
            curr.next = ListNode(1)

    
        return dummy.next
        