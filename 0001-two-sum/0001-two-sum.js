/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(let i=0; i<nums.length; i++){
        const find = target - nums[i]
        for(let j=i+1; j<nums.length; j++){
            if(nums[j] === find){
                return [i, j]
            }
        }
    }
};

// input is not sorted
// for i=0
// find is target - nums[i]
// for j=i+1
// if nums[j] is find
// return [i, j]
