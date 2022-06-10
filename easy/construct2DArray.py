class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n>len(original) or m*n<len(original):
            return []
        twod=[[0 for i in range(n)] for j in range(m)]
        k=0
        for i in range(m):
            for j in range(n):
                twod[i][j]=original[k]
                k+=1
        return twod