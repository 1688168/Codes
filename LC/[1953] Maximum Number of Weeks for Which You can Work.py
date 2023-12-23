class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        """
        # Template
        * a list of projs (English letters)
        * each proj has multiple milestones (num of repeating letters)
        * tasks from same proj (chars of same letter) need to have gaps (given a gap k)
        * max num of cycle (weeks) we can work on the projs without violating the Gapping rule?

        # complexity
        projs: 10^5     -> nlogn
        projs[i]: 10^9  -> O(N)

        # if we use greedy with heap
        * every proj enqueue (nlogn)
        * dq. to hold k
        * each proj need to be enqueue 10^9 times -> 

        # Observations:
        - k=1 (gap=1)
        - we do not need to output the actual task arrangement, just need to output count
        - Greedy: can we finish the max_freq?
        """

        


        N = len(milestones)

        # find the max freq
        max_freq = max(milestones)
        ttl_milestones = sum(milestones)

        remaining = ttl_milestones-max_freq
        if remaining >= max_freq:  # can you finish the max_freq?
            return ttl_milestones  # if we can finish the max_freq, we can finish all milestones
        else:
            # we cannot finish the max_freq, we will drop everything after using max_freq milestones filling the gabs
            return 2*remaining+1
