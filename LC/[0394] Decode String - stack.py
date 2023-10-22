class Solution:
    def decodeString(self, s: str) -> str:
        stk_str=[]
        stk_n=[]
        N = len(s)
        text=""
        ii=0
        while ii < N:
            if s[ii].isdigit():
                n=0
                while ii < N and s[ii].isdigit():
                    n = n*10 + int(s[ii])
                    ii+=1
            
                stk_n.append(n)
                stk_str.append(text)
                text=""
            
            elif s[ii]=="]":
                n=stk_n.pop()
                ss=stk_str.pop()
               
                text = ss+n*text

                ii+=1
            elif s[ii]=="[":
                ii+=1
            else:
                text += s[ii]
                ii+=1


        return text

                 

        