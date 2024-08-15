/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    // find middle
    let slow = head
    let fast = head.next
    while(fast && fast.next){
        slow = slow.next
        fast = fast.next.next
    }

    // reverse the second half
    let second = slow.next
    let prev = null
    slow.next = null // disconnect first and second half
    while(second){
        let temp = second.next // save the next
        second.next = prev // reverse the arrow
        prev = second // update prev
        second = temp // move over
    }

    // merge
    second = prev
    let first = head
    while(second){
        let temp1 = first.next
        let temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2
    }
    
};