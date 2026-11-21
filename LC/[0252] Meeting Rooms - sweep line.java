class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        List<int[]> events = new ArrayList<>();

        for(var pair: intervals){
            events.add(new int[]{pair[0], 1});
            events.add(new int[]{pair[1], -1});
        }

        int[][] events_arr = events.toArray(new int[0][]);
        Arrays.sort(events_arr, Comparator.comparingInt((int[] event) -> event[0])
                                          .thenComparingInt(event -> event[1]));
        //how to sort ArrayList
        // events.sort(Comparator.comparingInt((int[] event) -> event[0])
        //                       .thenComparingInt(event -> event[1]));

        int acc = 0;
        for(var event: events_arr){
            acc += event[1];
            if(acc > 1) return false;
        }

        return true;
    }
}