/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    const dp = new Array(amount + 1).fill(amount + 1)
    dp[0] = 0

    for(let a = 1; a <= amount + 1; a++){
        for(const coin of coins){
            if(a - coin >= 0){ // curr amount - coin
                dp[a] = Math.min(dp[a], (dp[a - coin] + 1)) // don't forget to count itself
            }
        }
    }
    return dp[amount] !== amount + 1 ? dp[amount] : -1
};