class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        # Manacher O(N) solution
        1. transform to odd string
        2. calculate p[i]: where p[ii] is the extended radius of the longest palindromic substring centered @ ii
        """
        t = "#"
        # per this conversion, S is guaranteed to be a "odd" len string
        for cc in s:  # we need to convert s="abc" => s="#a#b#c#" or s="bb" => s="#b#b#"
            t += (cc+"#")

        N = len(t)
        # initialize p[ii] where p[ii] is the extended radius of the longest palindromic substring centered @ ii
        p = [0]*N
        max_center = -1
        max_right = -1

        for ii in range(N):
            kk = 0
            if ii > max_right:  # not covered by previous radius
                kk = 0  # no prior info, kk start from zero
                while ii-kk >= 0 and ii+kk < N and t[ii-kk] == t[ii+kk]:
                    kk += 1
            else:
                """
                p[i]: extended radius of the longest palindromic substring centered at i
                A                 B
                1 2 3 4 5 6 7 8 9 0 1 2 3 
                x x x x x x x x x x x x x} x x x 
                          ^
                          ctr
                    j             i
                                        max_right
                """
                # we have some info from prev p[jj] so kk does not need to start from 0
                # jj = max_center - (ii-max_center)
                #    = 2*max_center-ii
                # min(radius_jj, not exceeding max_right-ii)
                kk = min(p[max_center*2-ii], max_right-ii)
                while ii-kk >= 0 and ii+kk < N and t[ii-kk] == t[ii+kk]:
                    kk += 1

            p[ii] = kk-1

            if ii + p[ii] > max_right:
                max_right = ii + p[ii]
                max_center = ii

        max_len = -1
        center = 0

        for ii in range(N):
            if p[ii] > max_len:
                max_len = p[ii]
                center = ii

        # remember we inserted "#" to make odd
        return s[center//2 - max_len//2: math.ceil(center/2+max_len/2)]
        # max_len is radius including '#', so is total len after removing '#'
