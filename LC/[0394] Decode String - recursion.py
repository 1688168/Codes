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
