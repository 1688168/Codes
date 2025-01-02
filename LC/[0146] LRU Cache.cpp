class LRUCache {
public:
    LRUCache(int capacity) {
        list<int> List;//maintain oldest/newest key order
        unordered_map<int, list<int>::iterator> key2iter; //k2list::iterator
        unordered_map<int, int> key2val; //k2v
        int cap;
    }
    
    int get(int key) {
        //if kv not existing
        if(key2val.find(key)==key2val.end()) return -1;

        //if kv existing
        //1. get the value
        //2. update order 
        auto iter = key2iter[key];
        List.erase(iter);
        List.push_back(key);//updated order

        //update k2iter
        key2iter[key] = --List.end(); //prev(List.end()) << maybe this is better

        return key2val[key];
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