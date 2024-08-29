/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const first = helper(nums.slice(0, -1))
    const second = helper(nums.slice(1))

    function helper(arr){
        const dp = new Array(arr.length).fill(0)
        dp[0] = arr[0]
        dp[1] = Math.max(arr[0], arr[1])
        for(let i = 2; i < arr.length; i++){
            dp[i] = Math.max(arr[i] + dp[i - 2], dp[i - 1])
        }
        return dp[arr.length - 1]
    }
    
    if(nums.length === 1){// because both first and second will eliminate the element as the first element and the last element
        return nums[0]
    }
    return Math.max(first, second) 
};