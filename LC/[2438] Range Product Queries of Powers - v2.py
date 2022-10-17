class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        1. find the power array: binary representation of those 1s
        2. calc presum of the powers
        3. calc queries and output results
        """

        powers=[]
        pi=[]
        res=[]

        # calc power
        nn=n
        ii=0
        while nn > 0:
            if nn%2==1:
                powers.append(pow(2, ii))
                pi.append(ii)
            ii+=1
            nn//=2

        #print("powers: ", powers, ' pi: ', pi)
        # presum
        presum_pi=[]
        for ii in range(len(pi)):
            presum_pi.append(pi[ii] if ii==0 else presum_pi[ii-1]+pi[ii])

        """
        : how many power_diff could you have?
        : min=1
        : max: 1+2+...+2^32 ~ 32^2
        : so we appromiximatly have 32^2
        """
        presum2val=[]
        M=pow(10, 9)+7
        for ii in range(pow(32, 2)):
            presum2val.append(1 if ii==0 else presum2val[ii-1]*2%M)

        # process query.
        """
        : 101110
        : range division = pre-division_b/pre-division_a
        : since power array are all power of 2s, we can first convert above to substraction of powers
        """

        for st, ed in queries:
            power_diff=presum_pi[ed] - (presum_pi[st-1] if st > 0 else 0)
            #print("power_diff: ", power_diff)
            #ans=pow(2, power_diff)%M
            ans=presum2val[power_diff]
            res.append(ans)


        return res
        
