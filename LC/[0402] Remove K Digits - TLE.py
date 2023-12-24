class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        * if K=1, which digit do we remove?
        => remove the first number that is not monotonically increase
        * do this k times

        """
        def remove_one_digit(n):
            nn = list(n)
            nn.append('0')
            nn = list(map(lambda x: int(x), nn))
            res = []
            for ii in range(1, len(nn)):
                if nn[ii] < nn[ii-1]:
                    res = nn[:ii-1]+nn[ii:]
                    break

            nn = 0
            for n in res[:-1]:  # this will remove leading zero
                nn = nn*10+n

            if nn == 0:
                return "0"

            ss = ""
            while nn > 0:
                dd = nn % 10
                ss += str(dd)
                nn //= 10

            return ss[::-1]

        for ii in range(k):
            num = remove_one_digit(num)

        return num
