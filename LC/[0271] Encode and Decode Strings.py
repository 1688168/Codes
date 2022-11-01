class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        strLen#str
        """
        res=""
        for s in strs:
            res += (str(len(s))+'#'+s)
        print(" encode: ", res)
        return res


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res=[]
        ll, rr, N = 0, 0, len(s)
        while rr < N:
            while rr < N and s[rr] !='#':
                rr += 1
            nn=int(s[ll:rr])
            ss=s[rr+1:rr+1+nn]
            res.append(ss)
            rr = rr+1+nn
            ll=rr

        return res



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
