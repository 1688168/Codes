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

    // Sort by time asc; for ties, put +1 before -1 (descending by inc),
    // matching: if (a.first != b.first) a.first < b.first else a.second > b.second
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        List<int[]> events = new ArrayList<>(); // [time, inc]
        for (List<Interval> emp : schedule) {
            for (Interval r : emp) {
                events.add(new int[]{r.start, +1});
                events.add(new int[]{r.end, -1});
            }
        }

        events.sort((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(b[1], a[1]); // inc desc: +1 before -1
        });

        int count = 0;
        Integer start = null; // start of a free interval (null means none yet)
        List<Interval> ret = new ArrayList<>();

        for (int[] e : events) {
            count += e[1];
            if (e[1] == -1 && count == 0) {
                // just transitioned to no active work intervals → free time starts
                start = e[0];
            } else if (e[1] == +1 && count == 1 && start != null) {
                // just transitioned from free (0) to busy (1) → free time ends
                int end = e[0];
                ret.add(new Interval(start, end));
                start = null;
            }
        }
        return ret;
    }
}