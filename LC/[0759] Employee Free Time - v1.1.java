/*
// Definition for an Interval.
class Interval {
    public int start;
    public int end;

    public Interval() {}

    public Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/

class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        //declear/define events
        List<int[]> events = new ArrayList<>();

        // convert schedules to events (sweep line)
        for(var a_schedule: schedule){//for each employee
            for(var working_interval: a_schedule){
                events.add(new int[]{working_interval.start, +1});
                events.add(new int[]{working_interval.end, -1});
            }
        }

        //sort the events. 
        events.sort((a, b)-> a[0]!=b[0]?Integer.compare(a[0], b[0]):Integer.compare(b[1], a[1]));

        // traverse through the events and construct the gaps
        List<Interval> res = new ArrayList<>();
        int cnt = 0;
        int start = -1;
        int end = -1;
        for(var event: events){
            int ts = event[0];
            int delta = event[1];
            cnt+= delta;
            
            if(delta == -1 && cnt == 0){
                start = ts;
            }else if(start != -1 &&cnt==1 && delta == 1){
                end = ts;
                res.add(new Interval(start, end));
            }
        }

        // return the gaps (reverse merged intervals)
        return res;
        
    }
}

/*
* Ask: given a list of employees and their work schedule
* find intervals of common free time from all employees
* 
* Ideas: 
* - this is the reverse of merge intervals. After merging all intervals,
* what are the gaps?
* - we actually do not need to merge intervals and find gaps after, we can just
* sweepline pattern and try to construct the gaps directly
* - How do we know this is about sweep line?
* - this is given intervals.
* - we have to somehow merge intervals.  the options are: 
* a. greedy, b. DP, c. sweepline
*/