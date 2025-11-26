class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []

        for num in nums:
            pos = bisect_left(tail, num)
            if pos == len(tail):
                tail.append(num)
            else:
                tail[pos] = num

        return len(tail)