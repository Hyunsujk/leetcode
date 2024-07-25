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
        if(map.has(n)){
            return map.get(n);
        }
        let copy = new Node(n.val);
        map.set(n, copy);
        copy.neighbors = n.neighbors.map(copyNode);
        
        return copy;
    }

    return copyNode(node);
};

// base case
// if no node, return null

// map to store copied node
// function copyNode
// if map has node, return map.get node
// if map doesn't have node
// create a new node, add the new node to map
// get the added node, and copy neighbors,
// node.neighbors.map(copy)
// return new node
// return copyNode(node)