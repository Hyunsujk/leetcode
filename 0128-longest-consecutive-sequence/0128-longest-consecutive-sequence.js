/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if(nums.length === 0){
        return 0
    }

    nums.sort((a,b) => a - b)
    const map = new Map()
    for(let i=0; i<nums.length; i++){
        map.set(nums[i], 1)
    }

    for(let i=0; i<nums.length; i++){
        if(map.has(nums[i]-1)){
            map.set(nums[i], 0)
        }
    }

    let maxCount = 1
    for(const n of nums){
        if(map.get(n) === 1){
            let sequence = 1
            while(map.has(n + sequence)){
                sequence++
            }

            maxCount = Math.max(sequence, maxCount)
        }
    }

    return maxCount
    
};

// base case
// if nums is empty return 0

// sort the nums
// go through nums and add it to map

// mark the starting point
// go through nums and if the map has nums[i] - 1
// set map nums[i] to 0

// count the sequence
// max count is 1
// for n of nums
// if map.get(n) is 1
// seqence is 1
// while map.has(n+sequence)
// sequence ++

// max count is max between sequence and max count

// return max count