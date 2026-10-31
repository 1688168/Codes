class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        digits_rev = digits[::-1]

        carry = 0
        for ii in range(len(digits_rev)):
            total = digits_rev[ii] + carry
            if ii==0: total+=1
            digits_rev[ii] = total%10
            carry = total//10
        
        if carry: digits_rev.append(carry)

        digits=digits_rev[::-1]
        return digits
        