/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let left = 0
    let right = 1
    let profit = prices[1] - prices[0]
    while(right < prices.length){
        if(prices[right] < prices[left]){
            left = right
        } else {
            profit = Math.max(profit, prices[right]-prices[left])
        }
        right++
    }
    return profit > 0 ? profit : 0
};

// left pointer idx 0
// right pointer idx 1
// profit is left pointer - right pointer
// while right pointer is within the range
// if right pointer is less than left pointer, left pointer move to right pointer spot
// else update profit