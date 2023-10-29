###############
# 20231029
###############

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        - colors = "abaca"
        - colors[i] is a lowercase English letter representing the color of the ith node in this graph
        - edges = [[0,1],[0,2],[2,3],[3,4]]

        => largest color frequency in any path
        -> only consider paths from leaf-to-leaf (maximize the possibility)
        a. build graph: Time/Space: O(N)
        b. for each leaf-node, BFS till end and count for color
        c. return the highest color frequency
        """
        N = len(colors)
        g = collections.defaultdict(set)
        _idt = {ii: 0 for ii in range(N)}

        for a, b in edges:
            g[a].add(b)
            _idt[b] += 1

        colors_set = set(list(colors))

        def bfs(a_color):
            idt = _idt.copy()  # make a local copy of idt since we are modifying it locally
            dq = collections.deque()
            # we cannot rely on parent color cnt to determin the max of curr node color cnt as we might reach current node from diff level
            node2color_freq = defaultdict(int)
            for ii, vv in idt.items():
                if vv == 0:
                    dq.append(ii)  # initialize the queue
                    if colors[ii] == a_color:
                        # initialize the color frequency for those enqueued
                        node2color_freq[ii] += 1
            color_cnt = 0
            node_cnt = 0

            while (sz := len(dq)) > 0:  # BFS until all nodes are visited or encounters cycle
                for _ in range(sz):
                    curr = dq.popleft()
                    node_cnt += 1  # count the node num for cycle detection
                    # when evaluating each curr node, we update the color cnt so far
                    color_cnt = max(color_cnt, node2color_freq[curr])

                    for c in g[curr]:
                        idt[c] -= 1

                        # color count is max(existing count, or parent_count + child_count if child color matches)
                        node2color_freq[c] = max(
                            node2color_freq[c], node2color_freq[curr]+(1 if colors[c] == a_color else 0))

                        if idt[c] == 0:
                            dq.append(c)

            if node_cnt != N:
                return -1
            return color_cnt

        mxf = -N  # since we could return -1, default to max -N.  this might not be necessary as we short-circute the return
        for a_color in colors_set:  # for each color perform topology sort to count max color and detect cycle
            cnt = bfs(a_color)  # BFS each color in order to detect cycle
            if cnt == -1:
                return -1  # short circute when encounter cycle
            mxf = max(mxf, cnt)

        return mxf


###################################
###################################
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
