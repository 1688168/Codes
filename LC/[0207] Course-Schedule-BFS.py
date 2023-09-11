from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        : Topology sort
        """
        # declare indgree table and graph
        g=defaultdict(set)
        idt={ii:0 for ii in range(numCourses)}

        # build the graph
        for aa, bb in prerequisites:
            g[aa].add(bb)
            idt[bb] += 1

        dq=deque()
        for kk, vv in idt.items():
            if vv==0: dq.append(kk)

        # BFS
        path=[]
        visited=set()
        while len(dq) >0:
            curr=dq.popleft()
            visited.add(curr)
            path.append(curr)

            for child in g[curr]:
                if child in visited: continue #not necessary in this question
                idt[child] -= 1
                if idt[child]==0: dq.append(child)

        if len(path) != numCourses: return False

        return True





        
