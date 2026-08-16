class Solution:
    def decodeString(self, s: str) -> str:
        # mental model
        ## curr_str+curr_num*[next]

        def dfs(ss):
            if str is None: return 0, ""
            N=len(ss)
            curr_num=0
            curr_str=""
            ii=0
            while ii < N: 
                cc = ss[ii]
                if cc.isdigit():
                    curr_num = 10*curr_num+int(cc)
                    ii+=1
                elif cc == "[":
                    jj, text = dfs(ss[ii+1:])
                    curr_str = curr_str + curr_num*text
                    curr_num=0
                    ii += (jj+1)
                elif cc=="]":
                    ii+=1
                    break
                else:
                    curr_str += cc
                    ii+=1
            #print("curr_str: ", curr_str)
            return ii, curr_str

        jj, ss = dfs(s)
        return ss

        