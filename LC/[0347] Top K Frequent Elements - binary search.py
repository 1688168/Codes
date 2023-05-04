
"""
* Binary Search alway suse this template
"""
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        TopK freq elements
        whenever we are looking for value -> can we leverage binary search?
        """
        val2Freq = Counter(nums) # Time: O(N), Space: O(N)

        def countFreqGE(ff):
            cnt=0
            for kk, vv in val2Freq.items():
                if vv >= ff:
                    cnt += 1
               
            return cnt


        ll, rr, ans = 0, len(nums), -1

        # Time: O(logN)
        # Search for a freq that has at least K elements with freq >= than it
        while ll <= rr: #we are approaching to the best answer, so we cannot return when equal
    
            mm = ll+(rr-ll)//2 
            #print("ll: ", ll, " rr: ", rr, " mm: ", mm)

            if countFreqGE(mm) >= k: #if freq is GE K -> mm could be an answer but keep reducing
                ans=mm
                ll=mm+1 

            else:
                rr=mm-1

        res = []
        for kk, vv in val2Freq.items():
            if vv >= ans:
                res.append(kk)
        return res











"""
* guess a frequency and see if we have it
"""

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        TopK freq elements
        whenever we are looking for value -> can we leverage binary search?
        """
        val2Freq = Counter(nums) # Time: O(N), Space: O(N)

        def countFreqGE(ff):
            cnt=0
            for kk, vv in val2Freq.items():
                if vv >= ff:
                    cnt += 1
               
            return cnt


        ll, rr = 0, len(nums)

        # Time: O(logN)
        # Search for a freq that has at least K elements with freq >= than it
        while ll < rr: #we are approaching to the best answer, so we cannot return when equal
    
            mm = rr-(rr-ll)//2 #can we ever meet ll=rr to exit?
            #print("ll: ", ll, " rr: ", rr, " mm: ", mm)

            if countFreqGE(mm) >= k: #if freq is GE K -> mm could be an answer but keep reducing
                ll=mm 
                # if we have more element with freq > k, 
                #    -> we need to increase mm_freq to reduce qualified elements
                # Since mm could be an answer so we do not increment ll
            else:
                rr=mm-1
        


        res = []
        for kk, vv in val2Freq.items():
            if vv >= ll:
                res.append(kk)
        return res



