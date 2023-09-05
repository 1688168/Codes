class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        child2parent = {}

        def find(a):
            if a == child2parent[a]:
                return a
            return find(child2parent[a])

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa < pb:
                child2parent[pa] = pb
            elif pb < pa:
                child2parent[pb] = pa
            else:
                pass
            return

        # build relation per equal expressions
        for exp in equations:
            a, b = exp[0], exp[3]
            if a not in child2parent:
                child2parent[a] = a
            if b not in child2parent:
                child2parent[b] = b
            if exp[1] == '=':
                if a < b:
                    child2parent[a] = b
                else:
                    child2parent[b] = a

        # check if non-equals conflicts with equals
        for exp in equations:
            if exp[1] == '=':
                continue
            a, b = exp[0], exp[3]
            if find(a) == find(b):
                return False

        return True

        # validate relation per non-equal expressions
