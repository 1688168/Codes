from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache=OrderedDict()
        self.capacity=capacity


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        if self.capacity==0: return

        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key]=value
        else:
            if len(self.cache) >= self.capacity:
                try:
                    self.cache.popitem(last=False)
                except Exception as e:
                    print("poping failed")
                    throw
            self.cache[key]=value







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)