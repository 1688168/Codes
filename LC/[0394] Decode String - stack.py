##################
# 20231106
###################
class Solution:
    def decodeString(self, s: str) -> str:
        ii = 0
        stk_n = []
        stk_s = []
        text = ""
        N = len(s)
        while ii < N:
            c = s[ii]
            if c.isdigit():
                n = 0
                jj = ii
                while jj < N and s[jj].isdigit():
                    jj += 1
                n = int(s[ii:jj])
                ii = jj
                # after num always follows "["

                continue
            elif c == "[":
                stk_n.append(n)
                stk_s.append(text)
                text = ""
            elif c == "]":
                n = stk_n.pop()
                ss = stk_s.pop()
                text = ss + n*text
            else:
                text += c
            ii += 1
        return text

###################################


class Solution:
    def decodeString(self, s: str) -> str:
        ii = 0
        stk_n = []
        stk_s = []
        text = ""
        N = len(s)
        while ii < N:
            c = s[ii]
            if c.isdigit():
                n = 0
                while ii < N and s[ii].isdigit():
                    n = 10*n + int(s[ii])
                    ii += 1
                # after num always follows "["
                stk_n.append(n)
                stk_s.append(text)
                text = ""
            elif c == "]":
                n = stk_n.pop()
                ss = stk_s.pop()
                text = ss + n*text
                ii += 1
            elif c == "[":
                ii += 1
            else:
                text += c
                ii += 1
        return text
