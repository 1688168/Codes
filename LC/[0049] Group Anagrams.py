from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g=defaultdict(list)
        for ss in strs:
            g["".join(sorted(list(ss)))].append(ss)

        res=[]
        for k, v in g.items():
            res.append(v)
        return res
