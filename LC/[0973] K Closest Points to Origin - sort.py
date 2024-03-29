class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        * N: 10^4
        * points[ii]=[xi, yi]
        * k
        => topK smallest
        0. sort: nlogn
            - calc distance: N
            - sort: nlogn
            - n^2logn
        1. heap
            - calc distance: N
            - heappush: logn
        2. binary search
            - 0~10^4: 32
            - count(N)
        3. Quick-Select: O(N): Avg
        """
        # sol1: sort
        dist=[[pow(x,2)+pow(y,2), (x, y)] for x, y in points]
        dist.sort(key=lambda x: x[0])

        return [pp for dist, pp in dist[:k]]


        