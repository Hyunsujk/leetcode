class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)
            happy = 0
            while n:
                one = n % 10
                happy += (one ** 2)
                n //= 10
            n = happy
        
        return n == 1
        
        
            