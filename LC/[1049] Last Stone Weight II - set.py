# ----------------
# 20240911
# ----------------
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        ss = set([0])
        for s in stones:
            ns=ss.copy()
            ss=set()

            for x in ns:
                ss.add(x+s)
                ss.add(x-s)


        ans=math.inf

        for x in ss:
            if x >=0 and x < ans: ans=x
        
        return ans


###################
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        stones[ii]=weight of the ith stone
        * pick any two stone and merge:
        -> you can always switch orderes when performing addition/substraction
        -> so the overall merge process can be modeled as:
        -> +/- a1 +/- a2 ...

        => min weight after merge => target sum closest to zero
        * 穷举法 （exhaustive method)
        """
        N = len(stones)  # 1~30
        all_combinations = set([0])  # be careful to initialize a zero element
        for w in stones:
            tmp_all = set()
            for ee in all_combinations:
                tmp_all.add(ee+w)
                tmp_all.add(ee-w)
            all_combinations = tmp_all

        all_res = [s for s in all_combinations if s >= 0]

        return min(all_res)
