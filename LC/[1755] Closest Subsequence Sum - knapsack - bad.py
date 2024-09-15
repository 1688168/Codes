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
        # max sum: 40*10^7 = 4*10^8
        offset = 10^9 # max goal
        dp=[-math.inf]*(offset*2+5)
        total = sum(nums)
        dp[offset]=0
        for ii, nn in enumerate(nums): #for each num by contribution method
            
            dp_new=[-math.inf]*(offset*2+5)#reset dp for next round
            for jj in range(-offset, offset+1, 1):
                if dp[jj+offset]==-math.inf: continue #cannot base on invalid base

                #skip
                dp_new[jj+offset] = max(dp_new[jj+offset], dp[jj+offset])

                #take   
                if -offset <=jj+nn <=offset:
                    dp_new[jj+nn+offset] = max(dp_new[jj+nn+offset], dp[jj+offset]+nn)
            dp=dp_new

        # # find the larget feasible sumA
        # for jj in range(goal, -offset-1, -1):
        #     if dp[jj+offset] != -math.inf:
        #         sumA=dp[jj+offset]
        #      break
        
        sumA=dp[goal+offset]

        # print("sumA: ", sumA, "goal+offset: ", goal+offset)
        # print("total: ", total)
        sumB=total-sumA
        return goal-total+sumB

        



        