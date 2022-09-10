class Solution:
    def calculate(self, s: str) -> int:
        """
        * integer division should truncate toward zero. <<< handle negative division property
        * integers and operators ('+', '-', '*', '/'), "spaces"
        * we do not have nested priority: nested * or /, only need a variable to function as stack
        * states:
        committed,pending,op
        when we see a num    => evaluate "pending = pending op num"
        when we see "+ or -" => committed=committed+pending
        when we see "*/"      => evaluate "pending = pending op num"
        ex: 3/2
        ii  committed   pending    op    num
        0   0           3          +     3
        1                          /
        2   0
        3                                2
                        1
        4. skip

        """
        # states
        N=len(s)
        ii=0
        op='+'
        committed=0
        pending=0

        def calc(num):
            nonlocal pending
            if op=='+':
                pending += num
            elif op=='-':
                pending -= num
            elif op=='*':
                pending *= num
            elif op=='/':
                sign=1 if pending*num >= 0 else -1
                #print("pending: ", pending, " num: ", num)
                pending = abs(pending)//abs(num) * sign
            else:
                raise Exception(f"""Invalid operator {op}""")
            return

        while ii < N:

            c=s[ii]
            if c==' ':
                ii+=1
                continue

            if c.isdigit(): #got a number
                # parse out the num,
                jj=ii
                while jj<N and s[jj].isdigit():
                    jj+=1

                num=int(s[ii:jj])
                calc(num)
                ii=jj

            else: # got operators
                ii+=1
                op=c

                if c in ('+', '-'):
                    committed += pending
                    pending=0


        return committed+pending

        
