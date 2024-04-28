class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        """
        + N stickers
        + target: chars
        => min num of stickers required to spell-out target
        + len(target)=15 (max)
        + NN=2^15 states
        + dp[ii]: the min number of cards required to spell-out state[ii]
        +for each sticker: 
            dp[ii] = min(dp[jj]+1, dp[ii]) where a sticker bring dp[jj] to dp[ii] 
        """
        N=len(target) # target len
        NN=(1<<N) # ttl number of states
        dp=[math.inf]*NN #declare dp
        dp[0]=0 # requires zero sticker to spell-out ""

        def get_new_state(state, sticker):
            for sc in sticker: # can this char in sticker contribute?
                for ii, cc in enumerate(target):
                    if (state>>ii & 1)==0 and sc==cc: #if not matched yet and current char from sticker matches the target char
                        state = state + (1<<ii)
                        break # sc from sticker cannot be used again
            
            return state


        for state in range(NN): #for each state
            # Given a state, see what each sticker can bring it to
            if dp[state]==math.inf: continue # this means un-reachable state,no need to process
            for sticker in stickers: 
                new_state = get_new_state(state, sticker)
                #print("future_state: ", future_state, "dp_size: ", len(dp))
                dp[new_state] = min(dp[new_state], dp[state]+1)

        return dp[-1] if dp[-1] != math.inf else -1