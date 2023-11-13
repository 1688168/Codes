class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        idt = collections.defaultdict(int)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
            idt[a] += 1
            idt[b] += 1

        dq = collections.deque()

        for kk, vv in idt.items():
            if vv == 1:
                dq.append(kk)
        mxl = 0

        def dfs(curr, lvl):
            nonlocal mxl
            # print("curr: ", curr, " lvl: ", lvl)

            mxl = max(mxl, lvl-1)

            if curr in visited:
                return
            visited.add(curr)
            for child in g[curr]:
                dfs(child, lvl+1)
        while dq:
            curr = dq.pop()
            # print(" ============= curr: ", curr)
            visited = set()
            dfs(curr, 0)
            # print(" mxl: ", mxl)

        return mxl
