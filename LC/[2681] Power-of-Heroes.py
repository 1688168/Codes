M = pow(10, 9) + 7

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        ans=0
        nums.sort()
        N=len(nums)

        """
         0 1 2 3 4
         a b c d e

         ii    mx   mn     add              acc    
         0     a^2  a                            
                                            0
         1     b^2  b      self: b^2*b                                          
                    a      prev: b^2*a*1        <<< self^2*self+self^2*prev*1 + self^2*acc*2
                                            a   <<< acc= acc+prev
         2     c^2  c      self  c^2*c          < self^2*self
                    b            c^2*b*1        < self^2*prev*1
                    a            c^2*a*2        < self^2*acc*2
                                            
         3     d^2  d            d^2*d      
                    c            d^2*c 
                    b            d^2*b*2 
                    a            d^2*a*4
        
        """
        acc=0
        for ii in range(N): # for each ii as the max 
            mx=nums[ii]*nums[ii]%M # 9
            if ii >= 1:
                acc=(acc*2+nums[ii-1])%M     # acc=1 = 1*2+2=5        
            ans += (mx*nums[ii] + mx*acc)%M  # 
            ans %= M
    
        return ans%M