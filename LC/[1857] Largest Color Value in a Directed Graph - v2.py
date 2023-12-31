from collections import defaultdict, deque
from pprint import pprint as pp


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)  # get number of nodes
        # need to update all color count when visiting each node
        color_set = set(colors)
        # build graph and idt
        # probably don't need this as we only traverse once
        idt = {ii: 0 for ii in range(N)}
        g = defaultdict(set)  # initialize the graph
        for a, b in edges:  # build the graph
            g[a].add(b)
            idt[b] += 1  # build the in-degree-table

        def bfs():
            """
            from edge node topology sort for all nodes and calc the color freq on each node
            """
            # prepare BFS DQ
            # initialize dq with zero indegree nodes
            dq = deque([cc for cc, ff in idt.items() if ff == 0])
            node2color2freq = defaultdict(lambda: defaultdict(int))
            for nn in dq:
                for color in colors:  # initialize color freq for each node before entering the BFS loop
                    node2color2freq[nn][color] = 1 if color == colors[nn] else 0

            color2max_freq = defaultdict(int)
            cnt = 0  # for cycle detection
            # print(" the graph: ")
            # pp(g)
            # pp(dq)
            curr = 0
            while (sz := len(dq)) > 0:  # we actually do not need the sz, but leave it here
                curr = dq.popleft()
                # print(" curr: ", curr, " prev: ", prev)
                cnt += 1  # node count for cycle detection
                for color in color_set:  # update all max_color freq for each processing node
                    color2max_freq[color] = max(color2max_freq.get(
                        color, 0), node2color2freq[curr][color])

                # print(" curr color counts")
                # pp(node2color2freq[curr])
                for child in g[curr]:
                    # each parent need to pass it's color info to it's child. so we always maintian max_color_freq from all path with parents (having same color) in diff level. <<<< this is where I struggled the most
                    for color in color_set:
                        color_match = 1 if color == colors[child] else 0
                        node2color2freq[child][color] = max(node2color2freq[child].get(
                            color, 0), node2color2freq[curr].get(color, 0)+color_match)

                    # typical BFS template adding child when idt==0
                    idt[child] -= 1
                    if idt[child] == 0:
                        dq.append(child)
            # print(" cnt: ", cnt, " dict: ", color2max_freq)
            # print(" node2color2freq: --- ")
            # pp(node2color2freq)
            if cnt != N:
                return None
            return color2max_freq

        # one topology sort and count each color on each node
        color2max_freq = bfs()  # we will get back color2maxfreq or None if cycle detected
        if color2max_freq is None:
            return -1
        max_color_code = -1
        max_color_freq = 0
        # findout the max_freq
        for cc, ff in color2max_freq.items():
            if ff > max_color_freq:
                max_color_freq = ff
                max_color_code = cc
        return max_color_freq
