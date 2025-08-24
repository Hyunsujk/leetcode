class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        currPattern = []

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currPattern.append(1)
            elif nums[i] == nums[i-1]:
                currPattern.append(0)
            else:
                currPattern.append(-1)
        
        count = 0
        for i in range(len(currPattern)-len(pattern)+1):
            subarray = currPattern[i:i+len(pattern)]
            if subarray == pattern:
                count += 1
        
        return count