###########
# 20230912
###########

import random
from collections import defaultdict
class RandomizedSet:

    def __init__(self):
        self.vals=[]
        self.val2local=defaultdict(set)
        

    def insert(self, val: int) -> bool:
        if val in self.val2local: return False
        self.vals.append(val)
        self.val2local[val]=len(self.vals)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.val2local: return False
        val_idx = self.val2local[val]
        self.val2local[self.vals[-1]]=val_idx
        self.vals[val_idx]=self.vals[-1]
        del self.val2local[val]
        self.vals.pop()
        return True
        

    def getRandom(self) -> int:
        idx = random.randrange(0, len(self.vals))
        return self.vals[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



#################################
from random import random
class RandomizedSet:

    def __init__(self):
        self.val2idx={}
        self.vals=[]
        

    def insert(self, val: int) -> bool:
        """
        * Append @ the end of the list: O(1)
        * record the index of the value
        """
        if val in self.val2idx: return False
        self.vals.append(val)
        self.val2idx[val]=len(self.vals)-1

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.val2idx: return False
        idx=self.val2idx[val]
        last=self.vals[-1]
        self.val2idx[last]=idx
        self.vals[idx]=last
        self.vals.pop()
        del self.val2idx[val]
        return True
        

    def getRandom(self) -> int:
        idx=int(random()*len(self.vals))
        return self.vals[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()