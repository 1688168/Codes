class Solution:
    def lastStoneWeightII(self, stones):
        sums_of_groups = {0} # keep track candidates
        total = sum(stones)  # get total weight
        
        for weight in stones: #for each stone
            addition_sums_of_groups = set() #starting from empty for each stone
            for sum_of_group in sums_of_groups: #existing candidates
                if weight + sum_of_group <= total // 2:                    
                    addition_sums_of_groups.add(weight + sum_of_group)
                elif weight + sum_of_group == total // 2: #sum(A)=total/2 --> the rest is automatically in B
                    return 0
            sums_of_groups |= addition_sums_of_groups #merging existing candidate with new candidates
                    
        return min(abs(total - sum_of_group - sum_of_group) for sum_of_group in sums_of_groups)
        