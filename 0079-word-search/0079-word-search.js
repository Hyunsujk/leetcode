/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const rows = board.length
    const cols = board[0].length

    function helper(r, c, i){
        if(i === word.length){
            return true
        }
        if(r < 0 || c < 0 
        || r >= rows || c >= cols 
        || board[r][c] !== word[i] 
        || !board[r][c]){
            return false
        }

        const temp = board[r][c]
        board[r][c] = null
        const res = helper(r + 1, c, i + 1) 
                    || helper(r - 1, c, i + 1) 
                    || helper(r, c + 1, i + 1) 
                    || helper(r, c - 1, i + 1)
        board[r][c] = temp
        return res
    }

    for(let r = 0; r < rows; r++){
        for(let c = 0; c < cols; c++){
            if(board[r][c] === word[0]){
                if(helper(r, c, 0)){
                    return true
                }
            }
        }
    }
    return false
};