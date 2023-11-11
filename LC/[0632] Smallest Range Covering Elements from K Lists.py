class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        # get first element from each list
        mnq = [(lst[0], ii, 0) for ii, lst in enumerate(nums)]
        heapq.heapify(mnq)  # min heap
        mn, mx = mnq[0][0], max(mnq, key=lambda x: x[0])[0]  # initial range
        mn_range = mx-mn
        ll, rr = mn, mx  # initial answer
        while mnq:
            vv, ii, jj = heapq.heappop(mnq)
            if jj+1 >= len(nums[ii]):
                break  # we need to have representative from each list, so we cannot run out
            # next in line from the list of current min
            heapq.heappush(mnq, (nums[ii][jj+1], ii, jj+1))
            mn = mnq[0][0]  # new min after pop/push
            mx = max(mx, nums[ii][jj+1])  # new mx after pop
            if mx-mn < mn_range:
                mn_range = mx-mn
                ll, rr = mn, mx

        return (ll, rr)
