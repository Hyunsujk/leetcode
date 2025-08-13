class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        nl = len(nums)
        pl = len(pattern)

        def matches(start):
            for i in range(pl):
                if pattern[i] == 1 and nums[start+i+1] <= nums[start+i]:
                    return False
                if pattern[i] == 0 and nums[start+i+1] != nums[start+i]:
                    return False
                if pattern[i] == -1 and nums[start+i+1] >= nums[start+i]:
                    return False
            return True

        count = 0
        for i in range(nl-pl):
            if matches(i):
                count += 1
        
        return count
        