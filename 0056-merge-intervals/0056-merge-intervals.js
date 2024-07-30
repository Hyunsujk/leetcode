/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a,b)=>a[0]-b[0])
    const result = []
    let prev = intervals[0]

    for(let i=1; i<intervals.length; i++){
        if(prev[1] >= intervals[i][0]){
            prev[1] = Math.max(prev[1], intervals[i][1])
        } else {
            result.push(prev)
            prev = intervals[i]
        }
    }

    result.push(prev)
    return result    
};

// sort intervals
// prev is index 0
// i=1 i<intervals.length
// if prev end >= interval i start 
// update prev end to math max prev end, i end
// else // interval doesn't overlap
// push prev to result
// prev is interval

// push last interval(prev) to result
// return result