from collections import defaultdict
from pprint import pprint as pp
import random
class RandomizedCollection:

    def __init__(self):
        self.val2Locals=defaultdict(set)
        self.vals=[]
        

    def insert(self, val: int) -> bool:
        is_existing = True if val not in self.val2Locals else False
        self.vals.append(val)
        self.val2Locals[val].add(len(self.vals)-1)
    
        # print(" --- insert status --- ")
        # print(" vals: ", self.vals)
        # pp(self.val2Locals)
        # print(" --- end of insert ---")

        return is_existing

    def remove(self, val: int) -> bool:
        # print(" --- remove top status --- ")
        # print(" vals: ", self.vals)
        # pp(self.val2Locals)
     
        # print(" --- end of remove top ---")

        is_existing = True if val in self.val2Locals else False
        if not is_existing: return is_existing
        
        last_val = self.vals[-1] #last val in vals list
        last_local = len(self.vals)-1

        if last_val==val:
            self.val2Locals[last_val].remove(last_local)
            if len(self.val2Locals[val])==0:
               del self.val2Locals[val]
            self.vals.pop()
        else:
            curr_one_local = next(iter(self.val2Locals[val]))
            #print(" removing: ", val, " local: ", curr_one_local)
            self.vals[curr_one_local]=last_val

            # update last_val
            self.val2Locals[last_val].remove(last_local)
            self.val2Locals[last_val].add(curr_one_local)

            # update val to be removed
            self.val2Locals[val].remove(curr_one_local)
        
            if len(self.val2Locals[val])==0:
                del self.val2Locals[val]

            self.vals.pop()


            # print(" --- remove end status --- ")
            # print(" vals: ", self.vals)
            # pp(self.val2Locals)
            # print(" --- end of remove end ---")

        return is_existing
        

    def getRandom(self) -> int:
        rand = random.randrange(0, len(self.vals))

        return self.vals[rand]

        
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()