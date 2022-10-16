class MyCalendar {
private:
    map<int, int> st2ed;
public:

    MyCalendar() {
    }

    bool book(int start, int end) {
         /*
            1---4
               3----6
                      7-----9
        */
        auto itr = st2ed.upper_bound(start); //upper bound: first element greater than the input argument
        if(itr != st2ed.begin()){
            auto pre = prev(itr, 1); //how to move iterator backward
            if(pre->second> start) return false;
        }


        if(itr != st2ed.end()){
            if(itr->first < end) return false;
        }


        st2ed[start]=end;

        return true;

    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
