/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let components = 0
    const rows = grid.length
    const cols = grid[0].length
    for(let r = 0; r < rows; r++){
        for(let c = 0; c < cols; c++){
            if(grid[r][c] == 1){
                helper(r,c)
                components++
            }
        }
    }
    return components

    function helper(row, col){
        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || grid[row][col] == 0){
            return
        }
        grid[row][col] = 0
        helper(row - 1, col)
        helper(row + 1, col)
        helper(row, col - 1)
        helper(row, col + 1)
    }
};