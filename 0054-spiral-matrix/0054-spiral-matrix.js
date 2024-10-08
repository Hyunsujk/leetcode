/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let res = []
    let top = 0
    let bottom = matrix.length // one over
    let left = 0
    let right = matrix[0].length // one over

    while(left < right && top < bottom){
        // add top row
        for(let i = left; i < right; i++){
            res.push(matrix[top][i])
        }
        top++
        // add right col
        for(let i = top; i < bottom; i++){
            res.push(matrix[i][right - 1])
        }
        right--
        if(!(left < right && top < bottom)){
            break
        }
        // add bottom row
        for(let i = right - 1; i >= left; i--){
            res.push(matrix[bottom - 1][i])
        }
        bottom--
        // add left col
        for(let i = bottom - 1; i >= top; i--){
            res.push(matrix[i][left])
        }
        left++
    }
    return res
};