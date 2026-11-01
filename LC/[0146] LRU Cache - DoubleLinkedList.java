import java.util.HashMap;
import java.util.Map;

class Node {
    int key;
    int value;
    Node prev;
    Node next;

    Node(int key, int value) {
        this.key = key;
        this.value = value;
    }
}

class DoublyLinkedList {
    private final Node head;
    private final Node tail;

    DoublyLinkedList() {
        head = new Node(0, 0); // Dummy head
        tail = new Node(0, 0); // Dummy tail
        head.next = tail;
        tail.prev = head;
    }

    void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.prev = null;
        node.next = null;
    }

    void addToEnd(Node node) {
        Node last = tail.prev;

        last.next = node;
        node.prev = last;
        node.next = tail;
        tail.prev = node;
    }

    void moveToEnd(Node node) {
        remove(node);
        addToEnd(node);
    }

    Node popFront() {
        if (head.next == tail) {
            return null;
        }

        Node node = head.next;
        remove(node);
        return node;
    }
}

class LRUCache {
    private final int capacity;
    private final Map<Integer, Node> cache;
    private final DoublyLinkedList order;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.order = new DoublyLinkedList();
    }

    public int get(int key) {
        Node node = cache.get(key);
        if (node == null) {
            return -1;
        }

        order.moveToEnd(node);
        return node.value;
    }

    public void put(int key, int value) {
        Node node = cache.get(key);

        if (node != null) {
            node.value = value;
            order.moveToEnd(node);
            return;
        }

        node = new Node(key, value);
        cache.put(key, node);
        order.addToEnd(node);

        if (cache.size() > capacity) {
            Node lru = order.popFront();
            cache.remove(lru.key);
        }
    }
}