/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countComponents = function(n, edges) {
    const adjList = new Array(n).fill().map(() => [])
    const visited = new Array(n).fill(false)

    for(const [start, end] of edges){
        adjList[start].push(end)
        adjList[end].push(start)
    }

    function helper(node){
        visited[node] = true
        for(const nei of adjList[node]){
            if(!visited[nei]){
                helper(nei)
            }
        }
    }

    let components = 0
    for(let i = 0; i < n; i++){
        if(!visited[i]){
            helper(i)
            components++
        }
    }
    return components
};