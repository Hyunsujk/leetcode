class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def AtMostK(k):
            seen = defaultdict(int)
            count = 0
            left = 0

            for right, num in enumerate(nums):
                if seen[num] == 0:
                    k -= 1
                seen[num] += 1
            
                while k < 0:
                    seen[nums[left]] -= 1
                    if seen[nums[left]] == 0:
                        k += 1
                    left += 1
            
                count += right - left + 1
            
            return count
        
        return AtMostK(k) - AtMostK(k-1)




        