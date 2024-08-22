/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let res = []

    function dfs(i, slate, sum){
        if(sum === target){
            res.push([...slate])
            return
        }
        if(i >= candidates.length || sum > target){
            return
        }

        slate.push(candidates[i])
        dfs(i, slate, sum+candidates[i])
        slate.pop()
        dfs(i+1, slate, sum)
    }

    dfs(0, [], 0)
    return res
};