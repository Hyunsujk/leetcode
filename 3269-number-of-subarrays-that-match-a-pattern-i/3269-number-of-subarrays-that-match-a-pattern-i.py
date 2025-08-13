class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        numPattern = []

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                numPattern.append(1)
            if nums[i] == nums[i-1]:
                numPattern.append(0)
            if nums[i] < nums[i-1]:
                numPattern.append(-1)

        count = 0
        for start in range(len(numPattern) - len(pattern) + 1):
            if numPattern[start: start+len(pattern)] == pattern:
                count += 1
        
        return count