class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # sanity check on inputs
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
    
        M = len(grid)
        N = len(grid[0])

        # Each land cell is a DSU node.
        # Connected land cells share the same root.
        parent = {}  # maps each land cell id to its parent
        size = {}    # size[root] stores the component size for each root

        def get_gid(ii, jj):
            return ii * N + jj

        def Find(x):
            if x != parent[x]:
                parent[x] = Find(parent[x])  # path compression
            return parent[x]

        def Union(a, b):
            pa = Find(a)
            pb = Find(b)

            if pa == pb:
                return

            # Attach smaller component under larger component.
            if size[pa] < size[pb]:
                pa, pb = pb, pa 

            parent[pb] = pa
            size[pa] += size[pb]

        # Initialize only land cells as separate components.
        for ii in range(M):
            for jj in range(N):
                if grid[ii][jj] == '0':
                    continue
                gid = get_gid(ii, jj)
                parent[gid] = gid
                size[gid] = 1

        # Only check down and right to avoid duplicate unions.
        dirs = [(1, 0), (0, 1)]

        # Union adjacent land cells.
        for ii in range(M):
            for jj in range(N):
                if grid[ii][jj] == '0':
                    continue

                for dx, dy in dirs:
                    nx, ny = ii + dx, jj + dy

                    if nx < 0 or nx >= M or ny < 0 or ny >= N:
                        continue
                    if grid[nx][ny] == '0':
                        continue

                    Union(get_gid(ii, jj), get_gid(nx, ny))
        
        # Count distinct roots among all land cells.
        return len(set(Find(x) for x in parent))