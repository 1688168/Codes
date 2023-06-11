class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
           6 5 3 1 0
           3 1 1
        i  0 1 2 3 4
        h  1 2 3 1 
        hi 1 2 
        """
        citations.sort(reverse=True)
        N=len(citations)
        hidx=0
        for ii in range(N):
            hidx = max(hidx, min(ii+1, citations[ii]))
        
        return hidx