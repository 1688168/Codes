from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None

        if self.get(key) != -1:
            self.cache[key] = value
            return

        if len(self.cache) >= self.capacity:
            try:
                self.cache.popitem(last=False)
            except Exception as e:
                raise

        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
