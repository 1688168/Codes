# class Solution:
#     def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
#         stack=[0]
#         visited={0}

#         while stack:
#             room = stack.pop()
#             visited.add(room)
#             for kk in rooms[room]:
#                 if kk not in visited: stack.append(kk)
        

#         return len(visited) == len(rooms)
            

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        stack = [0]
        visited = {0}

        while stack:
            room = stack.pop()
            for kk in rooms[room]:
                if kk not in visited:
                    visited.add(kk)
                    stack.append(kk)

        return len(visited) == len(rooms)

"""
# we want to practice implement the DFS by iterative implementation
"""
        