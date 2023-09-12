from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        idt={}
        g=defaultdict(set)
        for n in range(numCourses):
            idt[n]=0

        for a, b in prerequisites:
            g[b].add(a)
            idt[a] += 1

        dq=deque()
        for ii, vv in idt.items():
            if vv==0:
                dq.append(ii)
        res=[]
        while len(dq) > 0:
            curr = dq.popleft()
            res.append(curr)
            for c in g[curr]:
                idt[c]-=1
                if idt[c]==0:
                    dq.append(c)
        
        if len(res)!= numCourses: return []

        return res