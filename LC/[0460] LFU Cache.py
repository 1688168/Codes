##########
# 20231030
##########
from pprint import pprint as pp
from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2freq = {}
        self.freq2kv = collections.defaultdict(collections.OrderedDict)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key2freq:
            return -1
        freq = self.key2freq[key]
        new_freq = freq+1

        # remove from old freq
        val = self.freq2kv[freq].pop(key)

        # add to new freq
        self.freq2kv[new_freq][key] = val

        # update freq
        self.key2freq[key] = new_freq

        # update min_freq
        if self.min_freq == freq and len(self.freq2kv[freq]) == 0:
            self.min_freq = new_freq

        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if self.get(key) != -1:  # here we updated all freq relationship
            freq = self.key2freq[key]
            # then we update it's value under new freq
            self.freq2kv[freq][key] = value
            return

        else:
            if len(self.key2freq) >= self.capacity:
                least_freq_k, lest_freq_v = self.freq2kv[self.min_freq].popitem(
                    last=False)  # how to remove least freq
                del self.key2freq[least_freq_k]

            self.min_freq = 1
            self.key2freq[key] = 1
            self.freq2kv[1][key] = value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

##########
# 20221101
##########


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.k2f = {}
        self.f2kv = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.k2f:
            return -1

        ofreq = self.k2f[key]
        nfreq = ofreq+1

        # update f2kv to nf2kv
        val = self.f2kv[ofreq].pop(key)
        self.f2kv[nfreq][key] = val
        self.k2f[key] = nfreq
        if self.min_freq == ofreq and (len(self.f2kv[ofreq]) == 0):
            self.min_freq = nfreq

        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.k2f:
            freq = self.k2f[key]
            self.f2kv[freq][key] = value
            self.get(key)
        else:  # new key
            if len(self.k2f) >= self.capacity:
                least_freq_k, least_freq_v = self.f2kv[self.min_freq].popitem(
                    last=False)
                del self.k2f[least_freq_k]
            self.min_freq = 1  # new key
            self.k2f[key] = 1
            self.f2kv[1][key] = value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
###########################################################
###########################################################


class LFUCache:
    """
    : LFU
    : Given : (k, v)
    : * cache with LFU eviction policy, if same freq and LRU if freq is a tie
    : * given a key, we need to know freq in order to update, and value in order to return
    : * KF, KV
    : * KF map -> F:KV map  <<< the data structure
    : * in order to evict LRU if same freq, KV map need to be ordered
    : * in order to evict LF -> we need to know who is LF
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.k2f = {}
        self.f2kv = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if self.capacity <= 0:
            return -1  # boundary check on capacity

        f = self.k2f.get(key, -1)  # if key is not found, value is -1
        if f == -1:
            return -1

        # get kv map per frequency. should not be None
        kv = self.f2kv.get(f, None)

        if kv is None:
            return -1
        val = kv.pop(key)  # remove k from OrderedDict

        # update freq
        self.f2kv[f+1][key] = val
        self.k2f[key] = f+1

        if f == self.min_freq and (not self.f2kv[f]):
            self.min_freq += 1

        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.k2f:  # key existing, no eviction required
            # update value
            freq = self.k2f[key]
            kv = self.f2kv[freq]
            kv[key] = value

            self.get(key)  # update freq via get
            # update freq order
            return

        # check if we have capacity
        if len(self.k2f) >= self.capacity:
            # evict least freq with least timestamp
            key_to_remove, value_to_remove = self.f2kv[self.min_freq].popitem(
                last=False)  # understand popitem
            del self.k2f[key_to_remove]

        # now we have capacity, let's insert
        self.min_freq = 1  # new item start from 1
        self.k2f[key] = self.min_freq

        self.f2kv[self.min_freq][key] = value
        return


####################################################
####################################################


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
        self.capacity = capacity
        self.minFreq = 0
        self.keyToFreq = {}
        self.freqToKV = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        # print(" ========== getting key: ", key)
        if key not in self.keyToFreq:
            return -1

        freq = self.keyToFreq[key]
        self.keyToFreq[key] += 1

        val = self.freqToKV[freq].pop(key)
        self.freqToKV[freq+1][key] = val  # added to the end

        if freq == self.minFreq and (not self.freqToKV[freq]):
            self.minFreq += 1

        # print(" minfreq: ", self.minFreq)
        # pp(self.keyToFreq)
        # pp(self.freqToKV)
        return val

    def put(self, key: int, value: int) -> None:
        # print(" ================= putting key: ", key, " value: ", value)
        if self.capacity <= 0:
            return

        if key in self.keyToFreq:  # update existing cache
            freq = self.keyToFreq[key]
            self.freqToKV[freq][key] = value
            self.get(key)  # force updating the freq
            return

        if len(self.keyToFreq) == self.capacity:
            keyToRemove, valueToRemove = self.freqToKV[self.minFreq].popitem(
                last=False)
            del self.keyToFreq[keyToRemove]

        self.minFreq = 1
        self.keyToFreq[key] = self.minFreq
        self.freqToKV[self.minFreq][key] = value

        # print(" minfreq: ", self.minFreq)
        # pp(self.keyToFreq)
        # pp(self.freqToKV)

        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
