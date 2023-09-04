class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res = []
        for n in candies:
            if n+extraCandies >= mx:
                res.append(True)
            else:
                res.append(False)
        return res
