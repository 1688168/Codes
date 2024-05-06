/*
 * 20240504
*/
class AllOne {  

    //list to maintain order and support O(1) insert/delete operations
    list<int> freq_list;

    //kv update, given a key, mapping to it's frequency
    unordered_map<string, int> key2freq; 

    //from freq to key set
    unordered_map<int, unordered_set<string>> freq2key_set; //given a frequency, mapping to a set of keys with this frequency

    //freq to list iterator: given a frequency, mapping to the iterator pointing to the node in the list
    unordered_map<int, list<int>::iterator> freq2iter;
    

public:
    AllOne() {
        freq_list.push_back(0);
        freq2iter[0]=freq_list.begin();
    }
    
    void inc(string key) {
        //current freq
        int freq = key2freq[key];//if key is not existing, we will get freq=0.  this is C++
        int new_freq = freq+1;

        //update key2freq
        key2freq[key]=new_freq;
        //remove from old set and add to new set
        freq2key_set[new_freq].insert(key);
        if(freq > 0)freq2key_set[freq].erase(key);
        
        if(freq2key_set[new_freq].size()==1){//we need a new node for this freq
            freq_list.insert(next(freq2iter[freq]), new_freq);
            freq2iter[new_freq]=next(freq2iter[freq]);
        }

        if(freq > 0 && freq2key_set[freq].size()==0){
            freq_list.erase(freq2iter[freq]);
        }
        
    }
    
    void dec(string key) {
        //current freq
        int freq = key2freq[key];//if key is not existing, we will get freq=0.  this is C++
        if(freq==0) return; //unlike inc, we just bail
        int new_freq = freq-1;
        
        //update key2freq
        key2freq[key]=new_freq;

        //remove from old set and add to new set
        if(new_freq > 0)freq2key_set[new_freq].insert(key);
        freq2key_set[freq].erase(key);//old freq must be existing otherwise we already returned from above
        
        if(new_freq > 0 && freq2key_set[new_freq].size()==1){//we need a new node for this freq
            freq_list.insert(freq2iter[freq], new_freq);
            freq2iter[new_freq]=prev(freq2iter[freq]);
        }

        if(freq2key_set[freq].size()==0){
            freq_list.erase(freq2iter[freq]);
        }
    }
    
    string getMaxKey() {
        if(freq_list.size()==1) return "";
        return *(freq2key_set[freq_list.back()].begin());
        
    }
    
    string getMinKey() {
        if(freq_list.size()==1) return "";
        return *(freq2key_set[*(++freq_list.begin())].begin());
        
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

/* ===================================================== */
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
