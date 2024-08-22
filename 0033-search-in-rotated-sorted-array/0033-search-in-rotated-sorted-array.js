/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0
    let r = nums.length -1

    while(l<=r){
        const mid = Math.floor(l + (r - l) / 2)
        if(nums[mid] === target){
            return mid
        }

        // mid is in left half // right is +++/---
        if(nums[l] <= nums[mid]){ // use l pointers for both if statements
            if(target < nums[l] || target > nums[mid]){ // search right
                l = mid + 1
            } else {
                r = mid - 1
            }
        } else { // mid is in right half // left is +++/---
            if(target > nums[r] || target < nums[mid]){ // search left
                r = mid - 1
            } else {
                l = mid + 1
            }
        }
    }
    return -1
    
};