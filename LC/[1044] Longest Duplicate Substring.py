class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
        1. to identify the len for of the duplicate substring -> binary search to guess
        """
        N = len(s)
        ll, rr = 1, N
        ans = ""

        def is_found(mm):
            """
            - define a window of length mm.
            - can we find a duplicate when sliding this window?
            - when sliding the window, apply sliding hash strategy to reduce operation cost
            """
            visited = set()
            base = 26
            hash = 0

            pow_base_len = 1

            for ii in range(mm):
                pow_base_len *= base

            for ii in range(N):
                hash = hash*base + (ord(s[ii])-ord('a'))

                if ii >= mm:  # remove the window start as it is out of scope now
                    hash = hash - pow_base_len*(ord(s[ii-mm])-ord('a'))
                if ii >= mm-1:  # the substring become effective ()
                    if hash in visited:
                        # print("--- found: ", ii, " s: ", s[ii-mm+1:ii+mm], " ii: ", ii, " mm: ", mm)
                        return s[ii-mm+1:ii+1]

                    visited.add(hash)
            return ""

        while ll <= rr:
            # guessing mm is the max len of the longest duplicate substring
            mm = ll+(rr-ll)//2

            if (res := is_found(mm)) != "":  # if found, can we do longer
                ans = res
                ll = mm+1
            else:  # too long, try shorter
                rr = mm-1

        return ans
