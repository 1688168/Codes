class Solution:

    def multiply_by_one_digit(self, num_rev, digit):
        carry=0
        res_rev=[]
        for ii, nn in enumerate(num_rev):
            total = digit*int(nn)+carry
            res.append(total%10)
            carry = total//10
        
        if carry > 0: res.append(carry)
        return "".join(res_rev)

    def add_two_nums(self, num1_rev, num2_rev):
        N1=len(num1_rev)
        N2=len(num2_rev)
        ii=0
        jj=0
        carry=0
        total=0
        res=[]
        while ii < N1 and jj < N2:
            n1=int(num1_rev[ii])
            n2=int(num2_rev[jj])

        if carry > 0: res.append(carry)
        

    def multiply(self, num1: str, num2: str) -> str:
        
        if num1=="0" or num2=="0": return "0"

        N1=len(num1)
        N2=len(num2)

        num1_rev = num1[::-1]
        num2_rev = num2[::-1]

        if N1 < N2:
            num1_rev, num2_rev = num2_rev, num1_rev
            N1, N2 = N2, N1
        
        res="0"
        # smaller num multiple larger num
        for scale, nn in enumerate(num2_rev):
            if nn=="0": continue

            product_rev = self.multiply_by_one_digit(num1_rev, int(nn))
            product_rev += "0"*scale
            res = self.add_two_nums(res[::-1], product_rev)

        return res