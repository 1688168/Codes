class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        g = collections.defaultdict(list)  # to group nums by mod k
        for nn in nums:
            g[nn % k].append(nn)

        # intra-group could have distance k, inter-group is free of distance K
        # processing each group and count k-free subset
        cnt = 1

        def helper(st, sz, path):
            if len(path) == sz:  # we reached the size
                return 1
            cnt = 0
            for ii in range(st, len(gp)):
                if not path or gp[ii]-path[-1] != k:  # skip diff as k
                    cnt += helper(ii+1, sz, path+[gp[ii]])

            return cnt

        for id, gp in g.items():  # processing each group
            gp.sort()  # sort so we can compare with previous
            local_cnt = 0  # capture how many subset in this group that is k-free?
            for sz in range(len(gp)+1):
                path = []
                local_cnt += helper(0, sz, path)  # intra-group is addition
            cnt *= local_cnt  # inter-group is multification

        return cnt
