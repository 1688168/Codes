class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        cnt = 0

        for ii, vv in enumerate(num):
            while stk and cnt < k and int(vv) < stk[-1]:
                stk.pop()
                cnt += 1

            stk.append(int(vv))

        while stk and cnt < k:
            stk.pop()
            cnt += 1

        ans = 0
        for n in stk:
            ans = ans*10 + n

        res = ""
        while ans > 0:
            n = ans % 10
            ans //= 10
            res += str(n)

        if res == "":
            return "0"
        return res[::-1]
