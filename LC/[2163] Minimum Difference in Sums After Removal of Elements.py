from heapq import heappush, heappop, heappushpop


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        1. right min with size N
        2. left max with size N
        3. output min diff with ii as the partition
        """
        N = len(nums)//3

        mxq = []
        mxs = []

        mnq = []
        mns = []

        ttl = 0
        # processing left
        for ii in range(2*N):  # from 0 to 2N-1
            if ii < N-1:
                ttl += nums[ii]
                heappush(mxq, -nums[ii])
            elif ii == N-1:
                ttl += nums[ii]
                heappush(mxq, -nums[ii])
                mns.append(ttl)
            else:
                out = -1*heappushpop(mxq, -nums[ii])
                ttl = ttl+nums[ii]-out
                mns.append(ttl)

        # print(" mns: ", mns)
        # processing right
        ttl = 0
        for ii in reversed(range(N, 3*N)):  # for the right 2N; => 1, 2
            if ii > 2*N:  # ii > 1
                ttl += nums[ii]
                heappush(mnq, nums[ii])
            elif ii == 2*N:  # ii=1
                ttl += nums[ii]
                heappush(mnq, nums[ii])
                mxs.append(ttl)
            else:
                out = heappushpop(mnq, nums[ii])
                ttl = ttl+nums[ii]-out
                mxs.append(ttl)

        mxs.reverse()  # N~2N-1
        # print(" mxs: ", mxs)
        ans = math.inf
        for ii in range(len(mns)):
            ans = min(ans, mns[ii]-mxs[ii])

        return ans
