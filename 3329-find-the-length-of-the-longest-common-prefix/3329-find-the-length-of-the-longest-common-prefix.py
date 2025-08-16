class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1_prefix = set()

        for i in range(len(arr1)):
            n = arr1[i]
            while n:
                arr1_prefix.add(n)
                n //= 10
        
        max_prefix = 0
        for i in range(len(arr2)):
            n = arr2[i]
            while n:
                if n in arr1_prefix:
                    max_prefix = max(max_prefix, n)
                    break
                else:
                    n //= 10
        
        
        return len(str(max_prefix)) if max_prefix != 0 else 0

