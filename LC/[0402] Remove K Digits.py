###################
# 20231224
###################
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        make the list of digits monotonically increase
        """
        nums = list(map(int, num))
        stk = []
        cnt = 0

        for ii, nn in enumerate(nums):
            while stk and nn < stk[-1] and cnt < k:  # curr n is less than prev
                stk.pop()  # remove the violator
                cnt += 1
            stk.append(nn)

        # if we still  not removing k digits, (due to lack of violator), remove the tails
        while cnt < k:
            cnt += 1
            stk.pop()

        # remove the leading zero by convert the int list to num
        nn = 0
        for ii, n in enumerate(stk):
            nn = nn*10+n

        # convert num nn back to str
        ss = ""
        while nn > 0:
            n = nn % 10
            nn //= 10
            ss += str(n)

        return ss[::-1] if ss != "" else "0"

###################
# 20231224
###################


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        - 12745
        to remove a digit to minimize the remaining num.
        7 is the one to be select
        after removing 7
        1245 is in monotonic increasing order
        -> try to make a number in monotonic increasing order will give us the smallest number after removing k
        """
        # maintain a stack from original num that is in monotonic increasing order after removing k digits

        stk = []
        N = len(num)
        nums = list(map(int, list(num)))  # convert to int list
        cnt = 0
        # removing those that violates monotonic increasing rule
        for ii, vv in enumerate(nums):
            while stk and vv < stk[-1] and cnt < k:  # do this only k times
                stk.pop()
                cnt += 1

            stk.append(vv)

        while stk and cnt < k:  # if we still have remaining k after making the num monotonic increasing, removing from tail
            stk.pop()
            cnt += 1

        # converting the list of num back to string of num (removing 0s in the front)
        nn = 0
        for ii, vv in enumerate(stk):
            nn = nn*10+vv
        res = ""

        while nn:
            res += str(nn % 10)
            nn //= 10

        if res == "":
            return "0"
        return res[::-1]
###################
# 20231108
###################


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        - 12745
        to remove a digit to minimize the remaining num.
        7 is the one to be select
        after removing 7
        1245 is in monotonic increasing order
        -> try to make a number in monotonic increasing order will give us the smallest number after removing k
        """
        # maintain a stack from original num that is in monotonic increasing order after removing k digits

        stk = []
        N = len(num)
        nums = list(map(int, list(num)))  # convert to int list
        cnt = 0
        for ii, vv in enumerate(map(int, list(num))):
            while stk and vv < stk[-1] and cnt < k:
                stk.pop()
                cnt += 1

            stk.append(vv)

        while stk and cnt < k:  # if we still have remaining k after making the num monotonic increasing, removing from tail
            stk.pop()
            cnt += 1

        # converting the list of num back to string of num (removing 0s in the front)
        nn = 0
        for ii, vv in enumerate(stk):
            nn = nn*10+vv
        res = ""

        while nn:
            res += str(nn % 10)
            nn //= 10

        if res == "":
            return "0"
        return res[::-1]

################################################


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
