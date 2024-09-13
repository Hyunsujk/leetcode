/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const check = new Set()
    for(const num of nums){
        if(check.has(num)){
            return true
        } else {
            check.add(num)
        }
    }
    return false
};