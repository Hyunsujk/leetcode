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
    let slow = head
    let fast = slow.next
    while(fast && fast.next) {
        slow = slow.next
        fast = fast.next.next
    }

    let second = slow.next
    slow.next = null
    let prev = null

    while(second){
        let temp = second.next
        second.next = prev
        prev = second
        second = temp
    }
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

// find middle with slow and fast
// slow is head and fast is slow.next
// while fast is not the last one or out of range
// slow moves one, fast moves two
// slow is the end of the first half

// reverse the second half
// second is slow.next
// disconnect first half from second half // slow.next is null
// prev is null
// while second
// save the list // temp is second.next
// reverse the arrow // second.next is prev
// update prev // prev is second
// update second // second is temp
// now prev is start of second half

// merge first and second intervally
// second is prev
// first is head
// while second
// save the next // temp 1 is first.next, temp 2 is second.next
// connect second to first next // first next is second
// connect second next with temp 1 // second next is temp 1
// first is temp 1, second is temp 2