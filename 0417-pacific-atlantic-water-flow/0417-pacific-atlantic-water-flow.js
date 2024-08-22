/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {
    let rows = heights.length
    let cols = heights[0].length
    let res = []
    let pac = new Array(rows).fill().map(() => new Array(cols).fill(0))
    let atl = new Array(rows).fill().map(() => new Array(cols).fill(0))

    //left & right
    for(let row = 0; row<rows; row++){
        dfs(row, 0, pac, heights[row][0])
        dfs(row, cols-1, atl, heights[row][cols-1])
    }
    //top & bottom
    for(let col = 0; col<cols; col++){
        dfs(0, col, pac, heights[0][col])
        dfs(rows-1, col, atl, heights[rows-1][col])
    }

    function dfs(row, col, ocean, prevHeight){
        if(row < 0 || row >= rows || col < 0 || col >= cols) return;
        if(prevHeight > heights[row][col]) return;
        if(ocean[row][col] == 1) return;
        ocean[row][col] = 1
        dfs(row + 1, col, ocean, heights[row][col])
        dfs(row - 1, col, ocean, heights[row][col])
        dfs(row, col + 1, ocean, heights[row][col])
        dfs(row, col - 1, ocean, heights[row][col])
    }

    for(let row=0; row < rows; row++){
        for(let col=0; col<cols; col++){
            if(pac[row][col] == 1 && atl[row][col] == 1){
                res.push([row,col])
            }
        }
    }
    return res
};