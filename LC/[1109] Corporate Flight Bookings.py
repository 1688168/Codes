class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        N = n
        res = [0]*N
        for st, ed, inc in bookings:
            res[st-1] += inc
            if ed-1 < N-1:
                res[ed] -= inc

        for ii in range(1, N):
            res[ii] = res[ii]+res[ii-1]

        return res
