##########
# 20240403
##########
class Solution:
    def partitionString(self, s: str) -> int:
        """
        # N: 10^5
        # Bruteforce: 
        - all substring: N^2
        # DP, binary search, greedy
        - binary search <<< 32N
        - greedy: partition with longest substring without repeating and return count. O(N)
        -> min # of substring
        """

        char_set = set()
        st = 0
        cnt = 1  # at leat one partition
        for ed, cc in enumerate(s):
            char_set.add(cc)
            if ed-st+1 > len(char_set):
                st = ed
                cnt += 1
                char_set = set([cc])

        return cnt

##########
# 20240106
##########


class Solution:
    def partitionString(self, s: str) -> int:
        visited = set()

        cnt = 0
        for ii, cc in enumerate(s):
            if cc in visited:
                cnt += 1
                visited = set([cc])
            else:
                visited.add(cc)
        return cnt+1

##########
# 20231007
##########


class Solution:
    def partitionString(self, s: str) -> int:
        """

        """
        N = len(s)
        mns = 0

        char2cnt = collections.defaultdict(int)
        ll = 0
        for ii, cc in enumerate(s):
            char2cnt[cc] += 1
            if ii-ll + 1 > len(char2cnt):
                char2cnt = collections.defaultdict(int)
                char2cnt[cc] += 1
                ll = ii
                mns += 1

        return mns+1
###########################


class Solution:
    def partitionString(self, s: str) -> int:
        gps = 1
        chars = set()
        N = len(s)
        for ii in range(N):
            c = s[ii]
            if c in chars:
                gps += 1
                chars = set()
                chars.add(c)
            else:
                chars.add(c)
        return gps


##################
class Solution:
    def partitionString(self, s: str) -> int:
        dic = {}
        c = 0
        for i in s:
            if (i in dic):
                c += 1
                dic = {}
                dic[i] = 1
            else:
                dic[i] = 1
        if len(dic) != 0:
            c += 1
        return c
