class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        int N = ranges.length;
        int[][] events = new int[N*2][2];

        //model the events
        for(int ii=0; ii<N; ++ii){//for each range, convert to events
            events[ii*2][0] = ranges[ii][0];
            events[ii*2][1] = 1;
            events[ii*2+1][0] = ranges[ii][1]+1;//+1 due to inclusive
            events[ii*2+1][1] = -1;
        }

        //sort the events
        Arrays.sort(events, (a, b)-> {return a[0]==b[0]? Integer.compare(b[1], a[1]):Integer.compare(a[0] , b[0]);});

        for( var x: events){
            System.out.println("(" + x[0] + ", " + x[1] + ")");
        }

        //sweep line
        int sum=0;
        boolean isLeftCovered=false;
        boolean isRightCovered=false;
        for(var x: events){
            if(x[0]<=left) isLeftCovered=true;
            if(x[0]>=right) isRightCovered=true;
            sum+=x[1];
            System.out.println("sum: " + sum);
            if(x[0]>=left && x[0] <= right && sum==0) return false;
        }
        return isLeftCovered&&isRightCovered&&true;
    }
}

// * given interval (aka range)
// * are all integers between (left, right) inclusive are covered by ranges?
// * are can all ranges merge into one interval? (no gap in between)
// * interval -> diff array