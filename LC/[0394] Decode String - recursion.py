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
