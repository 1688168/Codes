class AllOne {
    list<int>List; // ordered sequence of values
    unordered_map<string,int>key2val;   // key->val
    unordered_map<int,unordered_set<string>>val2set;  //val->set of keys
    unordered_map<int,list<int>::iterator>val2iter;   //val-> iterator in list
    
public:
    /** Initialize your data structure here. */
    AllOne() {
        List.push_back(0);
        val2iter[0] = List.begin();
    }
    
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    void inc(string key) 
    {
        int val = key2val[key];
        
        key2val[key] = val+1;
        
        val2set[val+1].insert(key);
        if (val>0) val2set[val].erase(key); //remove old frequency
            
        if (val2set[val+1].size()==1) //only one element in this frequency -> a new node in list
        {
            List.insert(next(val2iter[val]), val+1);
            val2iter[val+1] = next(val2iter[val]);
        }
            
        if (val>0 && val2set[val].size()==0) //old frequency is empty now
        {
            List.erase(val2iter[val]); //delete the node from list if empty
        }
        
        //cout<<"OK"<<endl;
            
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    void dec(string key) 
    {
        int val = key2val[key]; //get current frequency
        if (val==0) return;     //if not existing, just return
        
        key2val[key] = val-1;   //update frequency per decrement api
        
        if (val-1>0) val2set[val-1].insert(key); //insert new or update existing freq2keys
        val2set[val].erase(key);                 //remove from current set
            
        if (val-1>0 && val2set[val-1].size()==1) //this is a new node after decrement
        {
            List.insert(val2iter[val], val-1);
            val2iter[val-1] = prev(val2iter[val]);
        }
            
        if (val2set[val].size()==0) //this freq has no more keys, remove the node
        {
            List.erase(val2iter[val]);
        }
    }
    
    /** Returns one of the keys with maximal value. */
    string getMaxKey() 
    {
        if (List.size()==1)
            return "";
        else
            return *(val2set[List.back()].begin()); //back is value VS (begin/end) are iterator
    }
    
    /** Returns one of the keys with Minimal value. */
    string getMinKey() 
    {
        if (List.size()==1)
            return "";
        else
            return *(val2set[*(++List.begin())].begin());;//begin is iterator (begin, end)
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
