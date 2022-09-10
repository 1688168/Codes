class Solution:
    def calculate(self, s: str) -> int:
        """
        * contents of parenthesis need to be processes and then degrade to numbers outside of the parenthesis
        => when we reach parenthesis -> push current state to stack.
        * manually code stack
        * recursive and leverage the system stack
        strategy:
        1. process char by char
        2. skip space
        3. if parenthesis, push current state to stack
        4. process contents inside parenthesis like a new string.
        5. when we reach ")", pop the stack and resume calc

        Time: O(N)
        Space: O(N) the max stack
        """


        N=len(s)

        #define the state
        op='+'
        curr=0

        ii=0

        stack_num=[]
        stack_op=[]


        def calc(num):
            nonlocal curr
            if op=='+':
                curr += num
            elif op=='-':
                curr -= num
            # elif op=='*':
            #     curr *= num
            # elif op=='/':
            #     curr //=num
            else:
                print("invalid operator: ", op)
                raise Exception(f"invalid operator {op}")

            return curr


        while ii < N:
            c=s[ii]

            if c==' ':
                ii+=1
                continue # skip space

            if c.isdigit():
                #parse out the num
                jj=ii
                while jj<N and s[jj].isdigit():
                    jj+=1

                num=int(s[ii:jj])
                calc(num)
                ii=jj
                #each time we got a num, we update curr with curr_op

            else: #c is operator or ()
                ii+=1
                if c == '(':
                    stack_num.append(curr)
                    stack_op.append(op)
                    curr=0
                    op='+'
                elif c==')':
                    num=curr
                    curr=stack_num.pop()
                    op=stack_op.pop()
                    calc(num)
                elif c in ('+', '-'):
                    op=c
        return curr
