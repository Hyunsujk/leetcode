/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let res = nums.length
    for(let i=0; i<nums.length; i++){
        res += i - nums[i]
    }
    return res
};

// i from 0 til < length
// add i - nums[i] so add 0 til n-1 while subtracting what we really have.
// res start with nums.length
// return res