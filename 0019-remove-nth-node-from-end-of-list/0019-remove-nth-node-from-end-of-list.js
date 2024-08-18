/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let fast = head
    let slow = head
    for(let i=0; i<n; i++){
        fast = fast.next
    }
    if(!fast){
        return head.next
    }
    while(fast.next){
        fast = fast.next
        slow = slow.next
    }
    slow.next = slow.next.next
    return head
};

// create n gap between fast and slow
// if fast is null which means head node needs to be removed, return head.next
// move the pointers until the end // while fast.next move fast and slow to next
// slow is prev node of target
// update slow.next with slow.next.next
// return head