class DJS: #disjoint set
    def __init__(self, arr, capacity=100005):
        self.capacity=capacity
        self.parent_root=[None]*self.capacity
        self.rank=[None]*self.capacity

        for a in arr:
            self.parent_root[a]=a
            self.rank[a]=1


    def union(self, a, b):
        pa=self.find(a)
        pb=self.find(b)
        if self.rank[pa] <= self.rank[pb]:
            self.parent_root[pb]=pa
            self.rank[pa] += 1
        else:
            self.parent_root[pa]=pb
            self.rank[pb] += 1

    def find(self, n):
        if self.parent_root[n] != n:
            self.parent_root[n]=self.find(self.parent_root[n])

        return self.parent_root[n]


from collections import defaultdict
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """
        : 0. initialize the union. (go by index of vals - remember vals values have duplicates)
        : 1. build val2idx: multiple index of same value, so we build a reverse lookup table
        :   a. remove duplicates from val
        :   b. sort for increasing order
        : 2. build the connection graph
        :
        """
        N=len(vals)
        djs=DJS([ii for ii in range(N)])



        val2idx=defaultdict(list)
        for ii, vv in enumerate(vals):
            val2idx[vv].append(ii)

        valset=set(vals)#remove duplicate
        sorted_val=list(valset)
        sorted_val.sort() #we need to add val in the DJS in increasing order

        # print(" sorted_val: ", sorted_val)

        g=defaultdict(set) # given a value, what are the connected indexes?



        for aa, bb in edges:
            if vals[aa] > vals[bb]:  # we only keep the bigger value as vertex. so this answer given a bigger value, where does it connect to?
                 g[vals[aa]].add((aa, bb))
            else:
                 g[vals[bb]].add((bb, aa))

        # for k, s in g.items():
        #     print(" ---- val: ", k)
        #     for n in s:
        #         print(n, end='')
        #     print()


        ans=0
        for v in sorted_val: #for each value on the tree
            #what are the indexes connecting to this val?
            for (aa, bb) in g[v]: #since they are connected, we union them to the tree
                if djs.find(aa) != djs.find(bb): #if they are not already sharing the same ancestor => union
                    djs.union(aa, bb)

            # so now we have built disjoint sets up to v.  for each set, let's count how many idx of value v so we can calc the numbers of
            # good paths ending with v

            root2cnt={} #for each root of the disjoint set, how many end nodes with value v?

            # get all index of value=v out and count per root
            for ii in val2idx[v]:
                p=djs.find(ii)
                root2cnt[p] = root2cnt.get(p, 0)+1

            # for each root in existing sets so far, count how many ends with value v
            for rt, cnt in root2cnt.items():
                ans += (cnt*(cnt-1)//2)

        return ans+N
