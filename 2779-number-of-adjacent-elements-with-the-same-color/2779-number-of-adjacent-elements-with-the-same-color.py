class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n

        output = []
        matches = 0
        for i, c in queries:
            oldColor = colors[i]

            if i-1 >= 0:
                if colors[i-1] == oldColor != 0:
                    matches -= 1
                if colors[i-1] == c:
                    matches += 1
            if i+1 < len(colors):
                if colors[i+1] == oldColor != 0:
                    matches -= 1
                if colors[i+1] == c:
                    matches += 1
            
            colors[i] = c

            output.append(matches)
        
        return output
        