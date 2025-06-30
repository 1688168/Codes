import java.util.*;

class LRUCache {
    private int capacity;
    private Map<Integer, Integer> k2v;
    private LinkedList<Integer> keyOrderList;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.k2v = new HashMap<>();
        this.keyOrderList = new LinkedList<>();
    }

    public int get(int key) {
        if (!k2v.containsKey(key)) return -1;

        // Move key to end
        keyOrderList.removeFirstOccurrence(key);
        keyOrderList.addLast(key);

        return k2v.get(key);
    }

    public void put(int key, int value) {
        if (k2v.containsKey(key)) {
            // Update existing value
            k2v.put(key, value);
            get(key);
            return;
        }

        if (keyOrderList.size() == capacity) {
            Integer lruKey = keyOrderList.removeFirst();
            k2v.remove(lruKey);
        }

        k2v.put(key, value);
        keyOrderList.addLast(key);
    }
}

// ****************************
//the Following is NOT working
// ****************************
// class LRUCache {
//     private int capacity;
//     private Map<Integer, Integer> k2v;  //cache KV look up
//     private Map<Integer,  ListIterator<Integer>> k2itr;//maintain order
//     private LinkedList<Integer> keyOrderList;

//     public LRUCache(int capacity) {
//         this.capacity=capacity;
//         this.k2v = new HashMap<>();
//         this.k2itr = new HashMap<>();
//         this.keyOrderList = new LinkedList<>();
//     }
    
//     public int get(int key) {
//         if(!k2v.containsKey(key)) return -1;
//         //reorder
//         var itr = this.k2itr.get(key);

//         itr.remove();
//         this.keyOrderList.add(key);
//         ListIterator<Integer> iter = this.keyOrderList.listIterator(this.keyOrderList.size());
//         iter.previous();
//         this.k2itr.put(key, iter);

//         return this.k2v.get(key);
//     }
    
//     public void put(int key, int value) {
//         var val = this.get(key);
//         if(val!=-1){//existing key.  get method already updated order
//             this.k2v.put(key,value);
//             return;
//         }
//         //handle new key 
//         //should we evict old cache if exceeding capacity
//         if(this.keyOrderList.size() > this.capacity){
//             ListIterator<Integer> iter = this.keyOrderList.listIterator(0);
//             iter.next();
//             iter.remove();
//         }
      
//         this.k2v.put(key, value);
//         this.keyOrderList.add(key);
        
//         ListIterator<Integer> iter = this.keyOrderList.listIterator(this.keyOrderList.size());
//         iter.previous();
//         this.k2itr.put(key, iter);
//         return;
//     }
// }

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */