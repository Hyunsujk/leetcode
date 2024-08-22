/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
    if(!subRoot){
        return true
    }
    if(!root){
        return false
    }
    if(isSameTree(root, subRoot)){
        return true
    }

    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
};

function isSameTree(r, sub){
    if(!r && !sub){
        return true
    }
    if(r && sub && r.val == sub.val){
        return isSameTree(r.left, sub.left) && isSameTree(r.right, sub.right)
    }
    return false
}