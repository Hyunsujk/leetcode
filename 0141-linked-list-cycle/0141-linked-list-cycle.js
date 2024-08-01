/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    const visited = new Map()
    let node = head
    let pos = 1
    while(node){
        if(visited.get(node)){
            return true
        } else {
            visited.set(node, pos)
            node = node.next
            pos++
        }
    }
    return false  
};
// visited node, pos
// while next is not null, check if the node is visited
// if visited then has a cycle, return true
// if not visited, mark the node as visited
// update node with node.next

// return false