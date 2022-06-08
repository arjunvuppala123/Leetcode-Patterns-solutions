class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        while len(result) < n + 1:
            result = result + [x+1 for x in result]
        return result[:n+1]