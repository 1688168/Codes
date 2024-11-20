from collections import defaultdict
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        # build the adjacency list representation of the graph
        g = defaultdict(set)
        for aa, bb in edges:

            g[aa].add(bb)
            g[bb].add(aa)

        def bfs(start):
            """
             return the farthest node from the 'start' node
               and the distance between them.
            """
            visited = set()

            visited.add(start)
            dq = deque([start])
            distance = -1
            last_node = None
            while (sz:=len(dq)) > 0:
                for _ in range(sz):
                    curr = dq.popleft()
                    for neighbor in g[curr]:
                        if neighbor not in  visited:
                            visited.add(neighbor)
                            dq.append(neighbor)
                            last_node = neighbor
                distance += 1


            return last_node, distance

        # 1). find one of the farthest nodes
        farthest_node, distance_1 = bfs(0)
        # 2). find the other farthest node
        #  and the distance between two farthest nodes
        another_farthest_node, distance_2 = bfs(farthest_node)

        return distance_2
