/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const frequency = new Map()
    let bucket = []
    let res = []
    for(let i=0; i<nums.length; i++){
        frequency.set(nums[i], (frequency.get(nums[i]) || 0) + 1)
    }
    for(const [number, freq] of frequency){
        bucket[freq] = (bucket[freq] || new Set()).add(number)
    }
    for(let i=bucket.length-1; i>=0; i--){
        if(bucket[i]){
            res.push(...bucket[i])
        }
        if(res.length === k){
            return res
        }
    }
    
};

// count frequency of each number
// bucket sort by frequency
// from the end push, when length is k return array