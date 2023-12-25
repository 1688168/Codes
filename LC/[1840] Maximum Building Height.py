class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # it is not clear if the restriction list is sorted, so we sort
        # since postion zero is not in restriction, but it has to be zero
        restrictions.append([1, 0])
        restrictions.sort()  # sort by postition (1 indexed)
        M = len(restrictions)

        # h is zero indexed, restriction is 1 indexed
        # so we are operating on a much smaller data size (only those with restrictions)
        h = [0]*M

        # ii is index of restriction (not the iith building)
        """
        0 1 2 3
          ^   ^
          3   5

          5=3+(3-1)
        """
        # tww passes (same as 135) to determin the heights of all buildings with restriction
        for ii in range(1, M):  # here everybody is 1 indexed
            # h[0] is zero anyway
            h[ii] = min(restrictions[ii][1], h[ii-1]+restrictions[ii]
                        [0]-restrictions[ii-1][0])  # diff of position

        for ii in reversed(range(1, M-1)):
            h[ii] = min(h[ii], h[ii+1]+restrictions[ii+1][0] -
                        restrictions[ii][0])  # diff of position

        """
        h[i-1]+x =  h[i]+y    -- A
        pos[i-1]+x = pos[i]-y -- B

        => A+B => h[i-1]+ x + pos[i-1]+ x = h[i]+pos[i]
               x = c --- C

        y = h[i-1]+x - h[i] --- from A
          = h[i-1]-h[i] + x
          = h[i-1]-h[i] + C
          = h[i-1]-h[i] + (h[i]-h[i-1]+pos[i]-pos[i-1]) //2
          = (h[i-1]-h[i]+pos[i]-pos[i-1])/2

        """
        # find out the tallest buildings
        ans = 0
        for ii in range(1, M):
            # y = (h[ii-1]-h[ii] - (restrictions[ii-1][0]-restrictions[ii][0]))//2
            y = (h[ii-1]-h[ii]+restrictions[ii][0]-restrictions[ii-1][0])//2
            ans = max(ans, h[ii]+y)

        # last restriction might or might not be the last building. so, we could have building from last restriction to n
        ans = max(ans, h[M-1]+n-restrictions[M-1][0])
        return ans
