class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        - lowercase English letter (Try letter by letter)
        - color value: highest freq of color on a valid path 
        - return largest color value or -1 if exists cycle
        - for each in scope letter, dfs and count frequency.  capture the highest freq to return
        - use topology sort strategy to detect cycle
        """
        # prepare topology sort
        N = len(colors)
        g = collections.defaultdict(set)
        idt = {ii: 0 for ii in range(N)}
        for a, b in edges:
            g[a].add(b)
            idt[b] += 1

        color_set = set(list(colors))
        mxf = 0

        def bfs(color):
            freq = collections.defaultdict(int)
            idt2 = idt.copy()
            dq = collections.deque()
            for c, v in idt.items():
                if v == 0:
                    dq.append(c)
                    if colors[c] == color:
                        freq[c] += 1

            cnt = 0

            ret = 1
            while (sz := len(dq)) > 0:
                has_color = False
                for _ in range(sz):
                    curr = dq.popleft()
                    cnt += 1

                    for child in g[curr]:
                        idt2[child] -= 1

                        freq[child] = max(
                            freq[child], freq[curr] + (1 if colors[child] == color else 0))
                        ret = max(ret, freq[child])
                        # print(" child: ", child, " freq: ", freq[child], " color: ", color)
                        if idt2[child] == 0:
                            dq.append(child)

            if cnt != N:
                return -1
            return ret
        for color in color_set:

            ans = bfs(color)
            # print(" color: ", color, " ans: ", ans)
            if ans == -1:
                return -1
            mxf = max(mxf, ans)

        return mxf
