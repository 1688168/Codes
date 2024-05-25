class Solution:
    def rob(self, nums: List[int]) -> int:
        N=len(nums)

        def dp(is_first):
            tke=0
            ntk=0

            for ii, nn in enumerate(nums):
                tmp_tke=tke
                tmp_ntk=ntk
                if ii==0:
                    if is_first:
                        tke=nn
                        ntk=0
                    else:
                        tke=0
                        ntk=0
                elif ii==N-1:
                    if is_first:
                        continue
                    else:
                        tke=ntk+nn
                        ntk=max(tmp_tke, tmp_ntk)
                else:    
                    tke=tmp_ntk+nn
                    ntk=max(tmp_tke, tmp_ntk)
            return max(tke, ntk)

        return max(dp(True), dp(False))

        



        