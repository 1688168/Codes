from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(city: int) -> None:
            visited.add(city)

            for neighbor in range(n):
                if (
                    isConnected[city][neighbor] == 1
                    and neighbor not in visited
                ):
                    dfs(neighbor)

        provinces = 0

        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces