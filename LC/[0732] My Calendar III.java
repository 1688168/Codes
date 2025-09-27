class MyCalendarThree {
    Map<Integer, Integer> treeMap;//using sorted map
    public MyCalendarThree() {
        this.treeMap = new TreeMap<>();//this is sorted map
    }
    
    public int book(int startTime, int endTime) {
        this.treeMap.put(startTime, this.treeMap.getOrDefault(startTime, 0)+1);
        this.treeMap.put(endTime, this.treeMap.getOrDefault(endTime, 0)-1);
        int mx=0;
        int sum=0;
        for(var diff: treeMap.values()){
            sum += diff;
            mx=Math.max(mx, sum);
        }
        return mx;
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(startTime,endTime);
 */