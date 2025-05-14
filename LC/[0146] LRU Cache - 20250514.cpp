class LRUCache {
    list<int> list; //maintain order of key
    unordered_map<int, list<int>::iterator> key2iter; //from key to order list
    unordered_map<int, int> key2val;
    int cap;

public:
    LRUCache(int capacity) {
        this.cap = capacity;
        
    }
    
    int get(int key) {
        if(key2val.find(key)==key2val.end()){//not found
            return -1;
        }
 
        // return value and update LRU order
        auto iter = key2iter[key];
        list.erase(iter);
        list.push_back(key);
        key2iter[key] = --list.end(); //or use prev()
        
    }
    
    void put(int key, int value) {
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */