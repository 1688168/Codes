class Solution:
    def decodeString(self, s: str) -> str:
        # curr_str+curr_num*[next] --- defined the basic pattern/mental model
        # required data strucure
        curr_str = ""
        curr_num = 0
        stack=[]

        for cc in s: #traversing each char
            if cc.isdigit(): # accumulating curr_num
                curr_num = curr_num*10+int(cc)
            elif cc=="[": # push due to encountering a new structure
                stack.append((curr_str, curr_num))
                curr_str=""
                curr_num=0
            elif cc=="]": # pop
                prev_str, prev_num = stack.pop()
                curr_str = prev_str+prev_num*curr_str
            else: #chars
                curr_str += cc
        
        return curr_str