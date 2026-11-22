class Solution {
    public int minMeetingRooms(int[][] intervals) {

        if (intervals.length == 0) {
            return 0;
        }

        PriorityQueue<int[]> mnq = new PriorityQueue<>(intervals.length, Comparator.comparingInt((int[] pair)-> pair[1])
                                                                                   .thenComparingInt(pair->pair[0]));

        Arrays.sort(intervals, Comparator.comparingInt((int[] pair)-> pair[0]));

        for(var pair:  intervals){
            if(!mnq.isEmpty() && mnq.peek()[1] <= pair[0]){
                mnq.poll();
            }
            mnq.offer(pair);
        }
        return mnq.size();
    }
}