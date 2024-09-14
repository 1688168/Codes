"""
* partition nums to two subsets: A, B
* let sum(A) <= goal <= sum(B)
-> whenever being asked to partition a group into two subsets -> origin = A union B
-> Total=sum(A)+sum(B)
-> sum(A)=total-sum(B)
-> goal-sum(A)=goal-total+sum(B)
=> converting the problem to knapsack problem
* given a list of number
* capacity=goal
* the max total you can choose from the list of number that is <= goal
* return goal-total+sum(B)
-> potential goal 2*10^9 -> cannot do knapsack, memory exceed
"""
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        offset = 2^9*40
        dp=[-math.inf]*(offset*2+5)
        total = sum(nums)
        for ii, nn in enumerate(nums): #for each num by contribution method
            dp_old=dp.copy()
            dp=[-math.inf]*(offset*2+5)#reset dp for next round
            for jj in range(-offset, offset+1, 1):
                #if jj>goal: continue # we don't care about anything greater than goal
                if ii==0 and jj>= nn: #first item, as long as capacity allows
                    dp[jj+offset]=nn
                    continue
                if dp_old[jj+offset]==-math.inf: continue
                #skip
                dp[jj+offset] = max(dp[jj+offset], dp_old[jj+offset])
                #take
               
                if -offset <=jj+nn <=offset:
                    dp[jj+nn+offset] = max(dp[jj+nn+offset], dp_old[jj+offset]+nn)
     
        # # find the larget feasible sumA
        # for jj in range(goal, -offset-1, -1):
        #     if dp[jj+offset] != -math.inf:
        #         sumA=dp[jj+offset]
        #      break
        
        sumA=dp[goal+offset]
        if sumA==-math.inf: return abs(goal)
        # print("sumA: ", sumA, "goal+offset: ", goal+offset)
        # print("total: ", total)
        sumB=total-sumA
        return goal-total+sumB

        



        