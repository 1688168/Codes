class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        N=n
        events=[[0]*2 for _ in range(N*2+1)]

        for ii, (st, ed, nn) in enumerate(bookings):
            events[ii*2][0] = st
            events[ii*2][1] = nn
            events[ii*2+1][0] = ed+1 #be careful about when the subtraction should happen
            events[ii*2+1][1] = -nn
        
        events.sort(key=lambda x: (x[0], x[1]))

        ans=[0]*N

        for ts, delta in events:
            if ts-1 <N: #when we no longer care about who is leaving the flight
                ans[ts-1] += delta
        
        for ii in range(1, N):
            ans[ii] += ans[ii-1]
        
        return ans
