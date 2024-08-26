/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let goal = nums.length - 1
    for(let i = nums.length - 1; i >= 0; i--){ // start from the end and move the goal closer
        if(i + nums[i] >= goal){
            goal = i
        }
    }

    return goal === 0 ? true : false  
};