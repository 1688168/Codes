class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0]=="0" or num2[0]==0: return "0"

        def multiply_by_one_digit(num, digit):
            carry=0
            ans=""
            for ii in range(len(num)):
                curr_digit = int(num[ii])
                product = digit*curr_digit
                ans=ans+str(product%10)+carry
                carry = product/10
            
            if carry > 0:
                ans = ans + str(carry)
            
            return ans

        
        def aggregate_result(res, aa, scale):
            """
            res: accumulating result
            aa: product of single digit 
            sacle:
            """
            carry = 0
            N0 = len(res)
            N1 = len(aa)
            
        res=""
        num1_rev = reversed(num1)
        num2_rev = reversed(num2)

        scale=1
        for ii in range(len(num2_rev)):
            aa = multiply_by_one_digit(num1_rev, int(num2_rev[ii]))
            res = aggregate_result(res, aa, scale)

            scale *= 10

        return res

        