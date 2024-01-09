from collections import deque
from heapq import heappush, heappop, heappushpop
class DinnerPlates:

    def __init__(self, capacity: int):
        self.dq=deque()
        self.capacity=capacity
        self.mnh=[] # the left most non-full stack index
        self.mxh=[] #the right most non-empty stack index
        

    def push(self, val: int) -> None:
        if self.mnh: # the left most not-full stack
            idx=heappop(self.mnh) # get the left most empty stack
            self.dq[idx].append(val) # append new val
            if len(self.dq[idx]) < self.capacity: #still not full
                heappush(mnh, idx) # put it back to candidate
        else: #we do not have existing stack that is not full
            self.dq.append([val]) #append a new stack

            idx=len(self.dq)-1 # the index of current stack
            heappush(self.mnh, idx) # update the candidate stacks
            heappush(self.mxh, -idx)# update the candidate of right most non-emapty
    def pop(self) -> int:
        if len(self.dq)==0: return -1
        right_most_non_empty_idx=(-heappop(self.mxh))
        
        if len(self.dq[right_most_non_empty_idx])==0: return -1 #shouldn't happpen
        val=self.dq[right_most_non_empty_idx].pop()

        if len(self.dq[right_most_non_empty_idx]) > 0:
            heappush(self.mxh, -right_most_non_empty_idx)


        return val


    def popAtStack(self, index: int) -> int:
        if index >= len(self.dq): return -1 # index exceeding max current stacks

        stk=self.dq[index] # the current stack
        if not stk: return -1 # if this guy is empty, return -1
        
        # the target stack is NOT empty
        heappush(self.mnh, index) # update left most not full heap
        val=stk.pop() # get the value
        
        
        return val
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)