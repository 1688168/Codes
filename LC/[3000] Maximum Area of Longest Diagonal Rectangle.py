class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dimensions.sort(key=lambda x: (pow(x[0], 2)+pow(x[1], 2), x[0]*x[1]))
        return dimensions[-1][0]*dimensions[-1][1]
