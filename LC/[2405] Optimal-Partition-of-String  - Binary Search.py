class Solution:
    def partitionString(self, s: str) -> int:
        N = len(s)
        ll, rr, ans = 1, N, N

        def is_feasible(mm):
            char_set = set()
            st = 0
            cnt = 1
            for ii, cc in enumerate(s):
                char_set.add(cc)
                if ii-st+1 > len(char_set):
                    cnt += 1
                    if cnt > mm:
                        return False
                    char_set = set([cc])
                    st = ii

            return True

        while ll <= rr:
            mm = ll+(rr-ll)//2
            if is_feasible(mm):
                ans = mm
                rr = mm-1
            else:
                ll = mm+1

        return ans
