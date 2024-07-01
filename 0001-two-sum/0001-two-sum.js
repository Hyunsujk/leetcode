/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map()

    for(let i=0; i<nums.length; i++){
        if(map.has(target - nums[i])){
            return [map.get(target - nums[i]), i]
        } else {
            map.set(nums[i], i)
        }
    }
};

// use map
// for i=0
// if map has target-num[i]
// map get target-num[i]
// else
// map set num[i], i