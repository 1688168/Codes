class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Map<Integer, Integer> map = new TreeMap<>();
        for(var interval: intervals){
            map.put(interval[0], map.getOrDefault(interval[0], 0)+1);
            map.put(interval[1], map.getOrDefault(interval[1], 0)-1);
        }
        
        int sum=0;
        int mx=0;
        for(var diff: map.values()){
            sum+=diff;
            mx = Math.max(mx, sum);
        }
        return mx;
    }
}