/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a,b) => a[0]-b[0])
    const result = [intervals[0]]

    for(const int of intervals){
        const lastElementEndTime = result[result.length-1][1]
        if(int[0] <= lastElementEndTime){
            result[result.length-1][1] = Math.max(int[1], lastElementEndTime)
        } else {
            result.push(int)
        }
    }

    return result
};
