/**
 * // Definition for a _Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function(node) {
    if(!node){
        return null
    }
    const map = new Map();

    function copyNode(n){
        if(!map.has(n)){
            const copy = new Node(n.val)
            map.set(n, copy)
            copy.neighbors = n.neighbors.map(copyNode)
        }
        return map.get(n)
    }

    return copyNode(node);
};