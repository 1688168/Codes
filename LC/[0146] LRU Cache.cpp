class LRUCache {
private:
    list<int> List;//maintain oldest/newest key order
    unordered_map<int, list<int>::iterator> key2iter; //k2list::iterator
    unordered_map<int, int> key2val; //k2v
    int cap;
public:

    LRUCache(int capacity) {
        cap = capacity;
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

        //if key already existing, we can just leverage get to reorder and update
        if(get(key) != -1){//key existing.  get already managed ordering
            key2val[key] = value;
            return;
        }

        //if capacity is full, purge the least used one
        if(key2val.size() == cap){
            int key2Del = *List.begin();
            List.erase(List.begin());
            key2iter.erase(key2Del);
            key2val.erase(key2Del);
        }

        List.push_back(key);
        key2val[key] = value;
        key2iter[key] = --List.end();
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */