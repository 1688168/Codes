class Solution {
    public int minMeetingRooms(int[][] intervals) {
        List<int[]> events_list = new ArrayList<>();
        for(var pair: intervals){
            events_list.add(new int[]{pair[0], 1});
            events_list.add(new int[]{pair[1], -1});
        }
        int[][] events = events_list.toArray(new int[0][]);
        Arrays.sort(events, Comparator.comparingInt((int[] pair) -> pair[0])
                                      .thenComparingInt(pair -> pair[1]));
        int acc=0;
        int mx=0;
        for(var pair: events){
            acc+= pair[1];
            mx=Math.max(mx, acc);
        }
        
        return mx;
    }
}