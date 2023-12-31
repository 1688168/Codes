class Solution:
    def __init__(self):
        self.Father = {}

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        M = isConnected
        for ii in range(N):
            self.Father[ii] = ii

        def FindFather(ii):
            if self.Father[ii] != ii:
                self.Father[ii] = FindFather(self.Father[ii])
            return self.Father[ii]

        def Union(ii, jj):
            x = self.Father[ii]
            y = self.Father[jj]
            self.Father[x] = y

        for ii in range(N):
            for jj in range(N):
                if M[ii][jj] == 0:
                    continue

                if FindFather(ii) != FindFather(jj):
                    Union(ii, jj)

        families = set()
        for ii in range(N):
            self.Father[ii] = FindFather(ii)
            families.add(self.Father[ii])

        return len(families)
