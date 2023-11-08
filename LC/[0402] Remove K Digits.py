class Solution:
    """
    - if the digit stream is in increasing order, we will just remove the trailing numbers
    - per observation, we like to remove those numbers that violate the monotonick stream
    - monotonic stream => monotonic stack
    """

    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        cnt = 0

        for ii, vv in enumerate(num):
            # remove those that violates the increasing order
            while stk and cnt < k and int(vv) < stk[-1]:
                stk.pop()
                cnt += 1

            stk.append(int(vv))

        while stk and cnt < k:  # scanning through the stream and we still have unused k, remove the last digits
            stk.pop()
            cnt += 1

        ans = 0

        for n in stk:  # we can just cast by int, cuz we might have prfixing zeros
            ans = ans*10 + n

        # ValueError: Exceeds the limit (4300) for integer string co << we got this kind of error we trying casting to str
        # if ans =="": return "0"
        # return str(ans)

        # since we need to return in string, converting the number back to string
        res = ""
        while ans > 0:
            n = ans % 10
            ans //= 10
            res += str(n)

        if res == "":
            return "0"
        return res[::-1]
