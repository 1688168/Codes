###############
# 20231111
###############
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return None

        mxl = 1
        mxs = s[0]
        N = len(s)
        for ii, cc in enumerate(s):
            # odd case
            ll, rr = ii-1, ii+1

            while ll >= 0 and rr < N and s[ll] == s[rr]:
                if rr-ll+1 > mxl:
                    mxl = rr-ll+1
                    mxs = s[ll:rr+1]
                ll -= 1
                rr += 1

            # even case
            ll, rr = ii, ii+1
            while ll >= 0 and rr < N and s[ll] == s[rr]:
                ll -= 1
                rr += 1
            if rr-ll-1 > mxl:
                mxl = max(mxl, rr-ll-1)
                mxs = s[ll+1:rr]

        return mxs

###############
# 20230520
###############


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s is None:
            return None

        N = len(s)
        mxp = s[0]
        mxl = 0
        for ii in range(N):
            loc_len = 1
            jj, kk = ii - 1, ii + 1

            # odd case
            while jj >= 0 and kk < N and s[jj] == s[kk]:
                loc_len = kk-jj+1
                if loc_len > mxl:
                    mxp = s[jj: kk+1]
                mxl = max(mxl, loc_len)
                jj -= 1
                kk += 1

            # even case
            jj = ii-1
            kk = ii
            while jj >= 0 and kk < N and s[jj] == s[kk]:
                loc_len = kk-jj+1
                if loc_len > mxl:
                    mxp = s[jj: kk+1]
                mxl = max(mxl, loc_len)
                jj -= 1
                kk += 1

        return mxp


#################################
class Solution:
    def longestPalindrome(self, s: str) -> str:
        mxl = 0
        mxs = ""
        N = len(s)

        if len(s) == 1:
            return s

        for ii in range(N):
            l1 = 1
            jj, kk = ii, ii

            while jj >= 0 and kk < N and s[jj] == s[kk]:
                ll = kk-jj+1
                if ll > mxl:
                    mxl = ll
                    mxs = s[jj:kk+1]
                jj -= 1
                kk += 1

            jj, kk = ii-1, ii
            while jj >= 0 and kk < N and s[jj] == s[kk]:

                ll = kk-jj+1
                if ll > mxl:
                    mxl = ll
                    mxs = s[jj:kk+1]
                jj -= 1
                kk += 1

        return mxs

##########
# 20221029
##########


class Solution:
    def longestPalindrome(self, s: str) -> str:

        N = len(s)
        mxl = 0
        mxs = ""

        for ii in range(N):
            # anchor on each char
            # case 1: center
            if ii > 0:
                jj = ii-1
                kk = ii+1
                while jj >= 0 and kk < N and s[jj] == s[kk]:
                    if kk-jj+1 > mxl:
                        mxl = kk-jj+1
                        mxs = s[jj:kk+1]
                    jj -= 1
                    kk += 1
            else:
                mxl = 1
                mxs = s[0]

            # case 2: pair
            jj = ii+1
            kk = ii
            while jj < N and kk >= 0 and s[kk] == s[jj]:
                if jj-kk+1 > mxl:
                    mxl = jj-kk+1
                    mxs = s[kk:jj+1]

                kk -= 1
                jj += 1

        return mxs
