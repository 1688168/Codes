"""
Sol: using Single Sorted List (55.42%)
"""

from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        sl = SortedList(nums[:k])
        res=[]
        
        res.append(min(sl[x-1], 0))
        for ii in range(k, len(nums)):
            sl.remove(nums[ii-k])
            sl.add(nums[ii])
            res.append(min(sl[x-1], 0))
        
        
        return res
    
"""
sol: use bucket sort - 2 (72.8%)
"""

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        nums[i] between (-50, 50) -> bucket sort
        """
        res=[]
        buckets=[0 for _ in range(102)]
        
        def xth():
            count=0
            for ii in range(50):  # get out once we get in postive territory <<< 
                count += buckets[ii]
                if count >= x:
                    return min(0,ii-50)
            
            return 0                                
        
        for ii in range(k):
            buckets[nums[ii]+50] += 1
        
        res.append(xth())
        buckets[nums[ii-k+1]+50] -= 1
        
        for ii in range(k, len(nums)):
            buckets[nums[ii]+50] += 1
            res.append(xth())
            buckets[nums[ii-k+1]+50] -= 1                            
        
        return res
        

"""
sol: use bucket sort - 1 (25.91%)
"""
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        def xth():
            count=0
            for ii in range(102):
                if counter[ii] > 0:
                    count += counter[ii]
                    if count >=x:
                        return min(0, ii-50)
        
        
        counter = [0 for _ in range(102)]
        res=[]
        
        for ii in range(k): 
            counter[nums[ii]+50] += 1
        
        res.append(xth())
        for ii in range(k, len(nums)):
            counter[nums[ii]+50] += 1
            counter[nums[ii-k]+50] -= 1
            res.append(xth())
        
        return res


"""
20230429: this method is TLE
"""

from sortedcontainers import SortedList, SortedSet, SortedDict

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Tag: Dual PQ
        1. PBDS (RB-Tree -> Ordered_set.cpp)
        2. use buckets:
           * setup buckets from -50 ~ 50
           * update buckets when moving the sliding window
        3. two SortedList (C++ Multiset)
        
        -----
        related Q:
        -----
        1801.Number-of-Orders-in-the-Backlog (M)
        1882.Process-Tasks-Using-Servers (H)
        1942.The-Number-of-the-Smallest-Unoccupied-Chair (M+)
        2102.Sequentially-Ordinal-Rank-Tracker (H-)
        2402.Meeting-Rooms-III (M+)
        2653.Sliding-Subarray-Beauty (M+)
        """
        
        
        """
        Sol - two SortedList (C++ multiset):
        orderedSet=> SortedList
        
        Sol2:
        Use bucket solution        
        
        """
        
        def isInSl(sl, target):
            ll, rr, ans = 0, len(sl)-1, -1
            
            while ll <= rr:
                mm=ll+(rr-ll)//2
                
                if target == sl[mm]: return mm
            
                if sl[mm]> target:
                    rr=mm-1
                else:
                    ll=mm+1
                
            return ans
            
        
        sl1, sl2, res = SortedList(), SortedList(), []
        for ii, nn in enumerate(nums):
            #print(" ii: ", ii, " sl1: ", sl1, " sl2: ", sl2)
            if len(sl1) < x:
                sl1.add(nn)              
                        
            elif nn >= sl1[-1]:
                sl2.add(nn)
            else:
                sl2.add(sl1[-1])
                sl1.discard(sl1[-1])
                sl1.add(nn)
            
            #print(" ii: ", ii, " k: ", k, " ttl len: ", len(sl1)+len(sl2))
            if (len(sl1)+len(sl2)) >= k: #need to start to populate output
               
                if sl1[-1] < 0:
                    res.append(sl1[-1])
                else:
                    res.append(0)
                    
                #print("ii: ", ii, " res: ", res)
                """
                x=3
                k=4
                k 0 1 2 3 
                x 0 1 2
                toRemove = 3-4+1=ii-k+1
                  0 1 2 3 4 5
                """
                toBeRemoved=nums[ii-k+1]
                #is in sl1
                if (idx:=isInSl(sl1, toBeRemoved) != -1):
                    sl1.discard(toBeRemoved)
                    
                    if len(sl2) > 0:
                        sl1.add(sl2[0])
                        sl2.discard(sl2[0])
                else:
                    sl2.discard(toBeRemoved)
                                        
        return res
                
            