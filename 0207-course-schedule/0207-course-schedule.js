/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    const visited = new Set()
    const preReq = new Array(numCourses).fill().map(() => [])

    for(const [crs, pre] of prerequisites){
        preReq[crs].push(pre)
    }

    function dfs(crs){
        if(visited.has(crs)){
            return false
        }
        if(preReq[crs] == []){
            return true
        }

        visited.add(crs)
        for(const pre of preReq[crs]){
            if(!dfs(pre)){
                return false
            }
        }
        visited.delete(crs)
        preReq[crs] = []
        return true
    }    

    for(let i=0; i < numCourses; i++){
        if(!dfs(i)){
            return false
        }
    }
    return true
};