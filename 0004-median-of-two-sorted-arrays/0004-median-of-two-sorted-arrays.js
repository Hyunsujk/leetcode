/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let arrayA = nums1
    let arrayB = nums2

    // assign shorter array as array A
    const totalLength = arrayA.length + arrayB.length
    const halfSize = Math.floor(totalLength / 2)

    if(nums1.length > nums2.length){
        arrayA = nums2
        arrayB = nums1
    }

    let l = 0
    let r = arrayA.length - 1

    while(true){
        // find pointer for each array
        let aPt = Math.floor((l+r) / 2)
        let bPt = halfSize - (aPt + 1) - 1

        // divide left and right section for both array A and B
        let aLeft = aPt >= 0 ? arrayA[aPt] : Number.NEGATIVE_INFINITY
        let aRight = aPt + 1 < arrayA.length ? arrayA[aPt + 1] : Number.POSITIVE_INFINITY
        let bLeft = bPt >= 0 ? arrayB[bPt] : Number.NEGATIVE_INFINITY
        let bRight = bPt + 1 < arrayB.length ? arrayB[bPt + 1] : Number.POSITIVE_INFINITY

        // check if divided correctly
        if(aLeft <= bRight && bLeft <= aRight){
            if(totalLength % 2) {
                return Math.min(aRight, bRight)
            }
            return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight)) / 2
        } else if (aLeft > bRight) {
            r = aPt - 1
        } else {
            l = aPt + 1
        }
    }
    
};