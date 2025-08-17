# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        
        def add(head: ListNode, left: ListNode, right: ListNode, carry_over: int):
            left_val = left.val if left else 0
            right_val = right.val if right else 0
            total = left_val + right_val + carry_over
            if total >= 10:
                node_val = total % 10
                head.next = ListNode(node_val)
                head = head.next
                if left:
                    left = left.next
                if right:
                    right = right.next
                return add(head, left, right, 1)
            elif total > 0:
                node_val = total
                head.next = ListNode(node_val)
                head = head.next
                if left:
                    left = left.next
                if right:
                    right = right.next
                return add(head, left, right, 0)
            else:
                if left and right:
                    head.next = ListNode(total)


        add(dummy, l1, l2, 0)

        return dummy.next

        