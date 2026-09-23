
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited=set()

        def dfs(roomNum):
            for key in rooms[roomNum]:
                if key in visited: continue
                visited.add(key)
                dfs(key)

        visited.add(0)
        dfs(0)

        ## check which room is NOT invisited
        for ii in range(len(rooms)):
            if ii not in visited: return False

        return True

"""
# analysis
* room 0 is open and can be entered without a key
* each room has list of keys that we can use to enter other room ->  the connected rooms to the current roome
* can we enter all rooms -> can we dfs from room 0 and visit all rooms
* how do we know if we visited all rooms: we have a list of rooms (0, N-1) 
"""