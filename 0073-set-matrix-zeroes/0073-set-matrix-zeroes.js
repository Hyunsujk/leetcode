/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const rows = matrix.length
    const cols = matrix[0].length
    const list = []

    for(let r = 0; r < rows; r++){
        for(let c = 0; c < cols; c++){
            if(matrix[r][c] == 0){
                list.push([r,c])
            }
        }
    }

    list.map(x => helper(x[0], x[1]))

    function helper(row, col){
        for(let c = 0; c < cols; c++){
            matrix[row][c] = 0
        }
        for(let r = 0; r < rows; r++){
            matrix[r][col] = 0
        }
    }
    
};