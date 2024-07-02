/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const set = new Set(nums)
    let sequence = 0

    for(const num of nums){
        if(!set.has(num-1)){
            let count = 1
            while(set.has(num+count)){
                count++
            }
            sequence = Math.max(sequence, count)
        }
    }
    return sequence
};

// create set
// let sequence is 0

// iterate through nums
// if num is the lowest // !set.has[num-1]
// then count is 1
// while set.has[num+count]
// count ++
// sequence is math.max count, sequence
// return sequence