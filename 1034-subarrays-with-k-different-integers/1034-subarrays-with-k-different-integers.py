class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, distinct: int):
            seen = defaultdict(int)
            left = 0
            res = 0

            for right, num in enumerate(nums):
                if seen[num] == 0:
                    distinct -= 1
                seen[num] += 1
        
                while distinct < 0:
                    seen[nums[left]] -= 1
                    if seen[nums[left]] == 0:
                        distinct += 1
                    left += 1
                
                res += right - left + 1
            
            return res
        
        return atMostK(nums, k) - atMostK(nums, k-1)
        