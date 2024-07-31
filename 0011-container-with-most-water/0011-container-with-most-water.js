/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let lPt = 0
    let rPt = height.length-1
    let maxArea = 0

    while(lPt < rPt){
        const w = rPt-lPt
        const h = Math.min(height[lPt], height[rPt])
        maxArea = Math.max(maxArea, w*h)   
        if(height[lPt] < height[rPt]){
            lPt++
        } else {
            rPt--
        }  
    }
    
    return maxArea
};

// left pointer, right pointer
// max area 0
// while left pointer is less than right pointer
// if left pointer height is less than right pointer, left ++
// max area is max between maxArea and right pointer - left pointer * min of heights
// if right pointer height is less than left pointer, right --
// update max area