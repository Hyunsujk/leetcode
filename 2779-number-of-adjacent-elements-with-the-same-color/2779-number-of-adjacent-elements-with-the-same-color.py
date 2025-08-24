class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n

        output = []
        matches = 0
        for i, c in queries:
            oldColor = colors[i]

            if i-1 >= 0 and colors[i-1] == oldColor != 0:
                matches -= 1
            if i+1 < len(colors) and colors[i+1] == oldColor != 0:
                matches -= 1
            
            colors[i] = c

            if i-1 >= 0 and colors[i-1] == c:
                matches += 1
            if i+1 < len(colors) and colors[i+1] == c:
                matches += 1
            output.append(matches)
        
        return output
        