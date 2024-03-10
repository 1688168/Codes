from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        * routes[ii][jj]: iith bus, jjth stops
        *least number of buses -> shortest distance -> BFS
        -> BFS buses for shortest distance 
        """
        if source==target: return 0
        stop2bus=defaultdict(set)
        for ii, route in enumerate(routes):
            for stop in route:
                stop2bus[stop].add(ii)
        

        # BFS's best friend
        dq=deque([source])
        steps=0
        visited_stop=set()
        visited_bus=set()

        while (sz:=len(dq)) > 0:
            for _ in range(sz):# for all stops in this level
                curr_stop = dq.popleft()
                if curr_stop==target: return steps
                if curr_stop in visited_stop: continue#skip visited stop
                visited_stop.add(curr_stop)
                for a_bus in stop2bus[curr_stop]:
                    if a_bus in visited_bus: continue#skip visited bus
                    visited_bus.add(a_bus)
                    for stop in routes[a_bus]:
                        dq.append(stop)

            steps += 1

        return -1


        