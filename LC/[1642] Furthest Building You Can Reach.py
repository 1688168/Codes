from heapq import heappush, heappop, heappushpop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        # Given Resource/Rules -> how far can you go?
        - Greedy: apply a strategy 1 first and replace with strategy 2 when necessary
        1. move as far as you can with laddar
        2. when run out of ladder, replace prev min jump with bricks
        3. exit when run out of resources
        """
        N=len(heights)
        cnt=0
        mnq=[]
        ii=0
        for ii in range(1, N):
            prev=heights[ii-1]
            curr=heights[ii]
            diff = curr-prev
            if diff <=0: continue
            heappush(mnq, diff)

            # need to use resource
            # use laddar first
            if cnt < ladders:
                cnt+=1
            else:
                prev_min=heappop(mnq)
                if prev_min > bricks: return ii-1
                bricks-=prev_min

        return ii



        