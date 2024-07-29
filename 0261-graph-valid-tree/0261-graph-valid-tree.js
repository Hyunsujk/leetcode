/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean}
 */
var validTree = function(n, edges) {
    const adjList = new Array(n).fill().map(()=>[])
    for(const [start,end] of edges){
        adjList[start].push(end)
        adjList[end].push(start)
    }

    const visited = new Array(n).fill(0)
    const parent = new Array(n).fill(-1)

    function helper(node){
        visited[node] = 1
        for(const nei of adjList[node]){
            if(visited[nei] === 0){
                parent[nei] = node
                const sub = helper(nei) // check sub result
                if(sub === false){
                    return false
                }
            } else {
                if(parent[node] != nei){
                    return false
                }
            }
        }
        return true
    }

    let component = 0

    for(let i=0; i<n; i++){
        if(visited[i] === 0){
            const isTree = helper(i)
            component++
            if(component > 1 || !isTree){ // do early return
                return false
            }
        }
    }

    return true
    
};