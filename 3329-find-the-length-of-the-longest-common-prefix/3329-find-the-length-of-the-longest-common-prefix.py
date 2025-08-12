class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1_prefix = set()

        for n in arr1:
            while n:
                arr1_prefix.add(n)
                n = n // 10
            
        longest_prefix = 0
        for n in set(arr2):
            while n:
                if n in arr1_prefix:
                    longest_prefix = max(longest_prefix, n)
                    break
                n = n // 10

        return len(str(longest_prefix)) if longest_prefix != 0 else 0


        