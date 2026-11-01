class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def add_to_end(self, node):
        last = self.tail.prev

        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def move_to_end(self, node):
        self.remove(node)
        self.add_to_end(node)

    def pop_front(self):
        if self.head.next is self.tail:
            return None

        node = self.head.next
        self.remove(node)
        return node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.order = DoublyLinkedList()

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1

        self.order.move_to_end(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node is not None:
            node.value = value
            self.order.move_to_end(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self.order.add_to_end(node)

        if len(self.cache) > self.capacity:
            lru = self.order.pop_front()
            del self.cache[lru.key]