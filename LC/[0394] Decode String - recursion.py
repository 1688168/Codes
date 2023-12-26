##############
# 20231226
##############
class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s):
            text = ""
            N = len(s)
            ii = 0
            nn = 0
            while ii < N:
                cc = s[ii]
                if cc.isdigit():
                    jj = ii
                    while jj < N and s[jj].isdigit():
                        jj += 1
                    nn = int(s[ii:jj])
                    ii = jj
                    continue
                else:
                    if cc == "[":
                        ss, jj = helper(s[ii+1:])
                        text = text + nn*ss
                        ii += (jj+1)

                    elif cc == "]":
                        ii += 1
                        break
                    else:
                        text += cc
                        ii += 1
            return text, ii

        text, jj = helper(s)
        return text
##############
# 20231106
##############


class Solution:
    def decodeString(self, s: str) -> str:
        cs = ""
        ii = 0
        anum = 0
        N = len(s)
        while ii < N:
            char = s[ii]
            if char.isdigit():
                jj = ii
                while jj < N and s[jj].isdigit():
                    jj += 1
                anum = int(s[ii:jj])
                ii = jj
                continue
            elif char == "]":  # pop
                return cs, ii + 1  # this is the length ii travelled in this stack
            elif char == "[":
                substring, jj = self.decodeString(s[ii + 1:])
                cs += anum * substring
                anum = 0
                # ii need to increment 1 to move after "[" + jj the distance travelled in the recursion
                ii += (jj+1)
            else:  # a char
                cs += char
                ii += 1

        return cs


##################################
class Solution:
    def decodeString(self, s: str) -> str:
        cs = ''
        i = 0
        anum = 0

        while i < len(s):
            char = s[i]
            if char == "]":
                return cs, i + 1
            if char.isalpha():
                cs += char
                i += 1
            elif char.isdigit():
                anum = anum * 10 + int(char)
                i += 1
            else:
                substring, j = self.decodeString(s[i + 1:])
                cs += anum * substring
                anum = 0
                i += j + 1

        return cs
###############


class Solution:
    def decodeString(self, s: str) -> str:
        text = ""
        ii = 0
        n = 0

        N = len(s)
        while ii < N:

            c = s[ii]
            if c.isdigit():
                while ii < N and s[ii].isdigit():
                    n = n*10+int(s[ii])
                    ii += 1  # this will end at "["
            elif c == "[":
                ss, jj = self.decodeString(s[ii+1:])
                text = text + n*ss
                ii += (jj+1)
                n = 0
            elif c == "]":
                return text, ii+1
            else:
                text += c
                ii += 1
        return text
