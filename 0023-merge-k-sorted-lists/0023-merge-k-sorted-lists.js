/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    if(lists.length === 0){
        return null
    } 
    while(lists.length > 1){
        const list1 = lists.pop()
        const list2 = lists.pop()
        const merged = merge(list1, list2)
        lists.push(merged)
    }
    return lists[0]
};

function merge(list1, list2){
    let dummy = new ListNode()
    let head = dummy

    while(list1 && list2){
        if(list1.val <= list2.val){
            head.next = list1
            list1 = list1.next
        } else {
            head.next = list2
            list2 = list2.next
        }
        head = head.next
    }
    head.next = list1 || list2
    return dummy.next
}