class MyCalendarThree {
    map<int,int> Map;//in cpp, Map is sorted
public:
    MyCalendarThree() {
        
    }
    
    int book(int start, int end) {
        Map[start] += 1;
        Map[end] -= 1;
        int ret = 0;
        int sum = 0;
        for(auto & [ts, diff]: Map){
            sum += diff;
            ret = max(ret, sum);
        }
        return ret;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(startTime,endTime);
 */