class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = defaultdict(lambda: -1)
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                found = stack.pop()
                next_greater[found] = num
            stack.append(num)
        
        res = []
        for num in nums1:
            res.append(next_greater[num])
        return res
