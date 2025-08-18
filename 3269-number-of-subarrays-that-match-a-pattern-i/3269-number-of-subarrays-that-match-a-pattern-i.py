class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        curr_pattern = []
        
        for i in range(1, len(nums)):
            prev = nums[i-1]
            curr = nums[i]
            if curr > prev:
                curr_pattern.append(1)
            elif curr == prev:
                curr_pattern.append(0)
            else:
                curr_pattern.append(-1)

        count = 0
        for i in range(len(curr_pattern)-len(pattern)+1):
            if pattern == curr_pattern[i:i+len(pattern)]:
                count += 1

        return count
        