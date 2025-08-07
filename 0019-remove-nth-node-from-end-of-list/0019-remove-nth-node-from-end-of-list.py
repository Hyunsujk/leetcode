# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        curr = head
        target = length - n
        if n == length:
            return head.next
        if target == 0:
            return None

        while target - 1 > 0:
            curr = curr.next
            target -= 1
        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        return head

        
