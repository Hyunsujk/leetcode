class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        longest = 0
        for num in seen:
            if num-1 not in seen:
                count = 0
                while num in seen:
                    count += 1
                    num += 1
                longest = max(count, longest)
        
        return longest