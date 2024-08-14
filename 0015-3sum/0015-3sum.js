/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a,b) => a-b)
    let res = []

    for(let i=0; i<nums.length; i++){
        if(i > 0 && nums[i] === nums[i-1]){
            continue
        }

        let l=i+1
        let r=nums.length-1
        while(l<r){
            const threeSum = nums[i]+nums[l]+nums[r]
            if(threeSum > 0){
                r--
            } else if(threeSum < 0){
                l++
            } else {
                res.push([nums[i], nums[l], nums[r]])
                l++
                while(nums[l] == nums[l-1] && l < r){
                    l++
                }
            }
        }
    }
    return res
};

// sort the nums
// use i 0 til < length and do l, r pointers
// if i is same with previous, continue
// l is i +1, r is length-1
// while l < r
// three sum is i + l + r
// if sum is bigger than 0 then r --
// else if sum is less than 0 then l ++
// else which means is 0, push to result, l++
// while i is duplicate and <r, l++