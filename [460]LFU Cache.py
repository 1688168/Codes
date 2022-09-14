from collections import defaultdict, OrderedDict
from pprint import pprint as pp
class LFUCache:
    """
    : LFU
    : given K:V
    : capacity=c
    : get
    : -> update freq
    : put(K, V)
    : -> if exceeding capacity => eviction policy per freq.
    : -> insert/update freq
    : -> K2Freq
    : -> freq2KV
    : ---
    : if key is new.
    : k2Freq[key]=freq=1
    : freq2KV[1]=map[k]:v
    : if key is existing.
    : freq=k2Freq[key]
    : freq2KV[freq][K]=V
    """
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.minFreq=0
        self.keyToFreq={}
        self.freqToKV=defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        #print(" ========== getting key: ", key)
        if key not in self.keyToFreq: return -1

        freq=self.keyToFreq[key]
        self.keyToFreq[key] += 1

        val=self.freqToKV[freq].pop(key)
        self.freqToKV[freq+1][key]=val #added to the end

        if freq==self.minFreq and (not self.freqToKV[freq]): self.minFreq += 1

        #print(" minfreq: ", self.minFreq)
        #pp(self.keyToFreq)
        #pp(self.freqToKV)
        return val


    def put(self, key: int, value: int) -> None:
        #print(" ================= putting key: ", key, " value: ", value)
        if self.capacity <=0: return

        if key in self.keyToFreq: # update existing cache
            freq=self.keyToFreq[key]
            self.freqToKV[freq][key]=value
            self.get(key) #force updating the freq
            return


        if len(self.keyToFreq)==self.capacity:
            keyToRemove, valueToRemove=self.freqToKV[self.minFreq].popitem(last=False)
            del self.keyToFreq[keyToRemove]

        self.minFreq=1
        self.keyToFreq[key]=self.minFreq
        self.freqToKV[self.minFreq][key]=value

        #print(" minfreq: ", self.minFreq)
        #pp(self.keyToFreq)
        #pp(self.freqToKV)

        return




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
