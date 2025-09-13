



# DFS cycle detection
"""
- return True -> has cycle
         else -> no cycle
"""
from collections import defaultdict, deque

defaultdict(set)
visited={}
def has_cycle_dfs(curr):
    """
    return True if has cycle
        False otherwise
    :param curr:
    :return:
    """
    if curr in visited and visited[curr] == 1: return False
    if curr in visited and visited[curr] == 2: return True  # has cycle

    visited[curr] = 2
    for child in g[curr]:
        if has_cycle_dfs(child): return True
    visited[curr] = 1

    return False

N=10 #assuming we have 10 nodes
from collections import deque
N = numCourses
def has_cycle_bfs():
    """
    return True if the given graph has cycle
           False otherwise
    """
    dq = deque()

    idt = {ii: 0 for ii in range(N)}  # default indegree 0 for all nodes
    for ii in range(N):
        for c in g[ii]:
            idt[c] += 1
    res = []

    for n, v in idt.items():
        if v == 0: dq.append(n)

    while len(dq) > 0:
        curr = dq.popleft()
        res.append(curr)
        for c in g[curr]:
            idt[c] -= 1
            if idt[c] == 0:
                dq.append(c)

    return len(res) != N


def main():
    """
    The driver to call has_cycle_helper
    :return:
    """
    N=10 # number of nodes
    for n in range(N):
        if has_cycle_dfs(n): return True

    return False


