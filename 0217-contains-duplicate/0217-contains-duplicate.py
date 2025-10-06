class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = set(nums)
        return len(dup) != len(nums)