from collections import defaultdict
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        g=defaultdict(set)
        ans=0

        # converting the tree to graph as we need to traverse all branches
        for aa, bb in edges:
            g[aa].add(bb)
            g[bb].add(aa)


        def dfs(idx, parent):
            nonlocal ans
            val2cnt={} #given a value, what's the count in this branch?

            val2cnt[vals[idx]]=1

            for child in g[idx]: # traversing each child of the node
                if parent and child==parent: continue

                childVal2Cnt=dfs(child, idx)

                # remove those that is not qualifed for good path (stating from index, all children should be with value less than val of idx)
                for vv, ct in childVal2Cnt.items():
                    if vv < vals[idx]:
                        del childVal2Cnt[vv]


                # optimize lookup (use smaller one to look up bigger one to reduce number of lookup)
                if len(childVal2Cnt) > len(val2cnt):
                    childVal2Cnt, val2cnt = val2cnt, childVal2Cnt

                for vv, ff in childVal2Cnt.items():
                    if vv in val2cnt:
                        ans += ff*val2cnt[vv]


                for vv, ff in childVal2Cnt.items():
                    val2cnt[vv]=val2cnt.get(vv, 0) + ff


            return val2cnt



        dfs(0, None) # dfs from index=0 with parent=None
        


        return ans+len(vals)
