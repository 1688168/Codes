class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n2f = collections.Counter(nums)
        nf_list = [(ff, nn) for nn, ff in n2f.items()]
        nf_list.sort(key=lambda x: -x[0])

        res = []
        for ii in range(k):
            res.append(nf_list[ii][1])
        return res
