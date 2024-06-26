#############
# 20240420: refining the codes
#############
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        * N=12
        * K=12

          N 0 1 2 3 ...N
        k
        0
        1
        2
        3

        - encode tasks into binary representation in a int

        - 111111111111
        - iith bit indicate the iith task (12 tasks max)
        - each worker try all combination of jobs taken, and through the DP process we find the optima solution

        -> dp[ii][jj]: min time to complete all works represented as jj state with ii workers
        """
        N = len(jobs)
        NN = (1 << N)
        time = [0]*NN  # precalc time
        # here dp is initialized as math.inf
        dp = [[math.inf]*NN for _ in range(k+1)]

        for state in range(NN):  # for each state
            tt = 0
            subset = state  # do not overwrite original state for indexing
            for ii in range(N):  # for each bit in the state
                # be careful on the following two ways of bit operation
                if subset & 1:
                    tt += jobs[ii]  # Method 2
                subset >>= 1
                # if (state >> ii) & 1: tt += jobs[ii] # method 1

            time[state] = tt

        # set initial state
        dp[0][0] = 0  # zero workers to complete zero jobs -> time is zero

        for ii in range(1, k+1):  # for num of workers 0, 1, ..., k (inclusive)
            # each workder try all states and determine dp[ii][state]
            for state in range(NN):
                subset = state
                while subset > 0:
                    dp[ii][state] = min(dp[ii][state], max(
                        dp[ii-1][state-subset], time[subset]))
                    # how to iterate all subsets of a binary representation
                    subset = state & (subset-1)

        return dp[-1][-1]
#############
# 20240419: some modification to reduce space
#############


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        N = len(jobs)
        SN = pow(2, N)
        time = [0]*SN  # time[ii] is the required time to complete state[ii]
        # 12+1 rows for initial state, each worker has 4096 states (jobs finished)
        dp = [[math.inf]*SN for _ in range(k+1)]

        # precalc time for each state
        for state in range(1 << N):  # 0~2^N (not including)
            ttl_time = 0
            for ii in range(N):  # each state has N bits
                if ((state >> ii) & 1) > 0:  # which bit we perform the work? accumulate the time
                    ttl_time += jobs[ii]

            time[state] = ttl_time

        # special initail state: zero worker, zero jobs
        dp[0][0] = 0

        for ii in range(1, k+1):  # k workers given
            for state in range(1 << N):  # the inner two loop time is 3^N, (not 2^N*2^N)
                # iterate subset template: https://github.com/wisdompeak/LeetCode/blob/master/Template/Bit_manipulation/Iterate_Subsets.cpp
                # given a state, how to traverse the subset?
                # dp[ii][state]=math.inf
                subset = state
                while subset > 0:
                    dp[ii][state] = min(dp[ii][state], max(
                        dp[ii-1][state-subset], time[subset]))
                    #      ^^^ done w/o you ^^^ ^^^ your subset ^^^
                    subset = (subset-1) & state

        return dp[-1][-1]


########################
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        * NP question (expect small N) -> bruteforce
        * k<=12: max 12 workers
        * jobs <= 12: max 12 jobs
        * state=[010101010101]
        * eacher worker can take/no-take each job
        * each worker can work on: 2^12 states (each job take/no-take)
        dp[ii][state]: the minimum possible maximum working time of any assignment if we use i workers and get jobs of state done

        dp[ii][state]= min(max(dp[ii-1], time(subset))) # over all possible subset of state
        """

        """
        state = 1 0
        subset of (1,0): 10, 00
        subset of (0,1): 01, 00
        """
        time = [0]*4096  # time[ii] is the required time to complete state[ii]
        # 12+1 rows for initial state, each worker has 4096 states (jobs finished)
        dp = [[math.inf]*4096 for _ in range(14)]

        N = len(jobs)
        # precalc time for each state
        for state in range(1 << N):  # 0~2^N (not including)
            ttl_time = 0
            for ii in range(N):  # each state has N bits
                if ((state >> ii) & 1) > 0:  # which bit we perform the work? accumulate the time
                    ttl_time += jobs[ii]

            time[state] = ttl_time

        # special initail state: zero worker, zero jobs
        dp[0][0] = 0

        for ii in range(1, k+1):  # k workers given
            for state in range(1 << N):  # the inner two loop time is 3^N, (not 2^N*2^N)
                # iterate subset template: https://github.com/wisdompeak/LeetCode/blob/master/Template/Bit_manipulation/Iterate_Subsets.cpp
                # given a state, how to traverse the subset?
                # dp[ii][state]=math.inf
                subset = state
                while subset > 0:
                    dp[ii][state] = min(dp[ii][state], max(
                        dp[ii-1][state-subset], time[subset]))
                    #      ^^^ done w/o you ^^^ ^^^ your subset ^^^
                    subset = (subset-1) & state

        return dp[k][(1 << N)-1]
