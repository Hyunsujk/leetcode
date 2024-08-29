/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if(!head || !head.next){
        return head
    }
    let newHead = head
    if(head.next){
        newHead = reverseList(head.next)
        head.next.next = head // update next node's next to current node
    }
    head.next = null
    return newHead
};




