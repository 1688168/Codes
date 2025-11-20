class Solution {
    public int[][] averageHeightOfBuildings(int[][] buildings) {
        int N = buildings.length;

        // convert intervals to sorted events
        Map<Integer, long[]> events = new TreeMap<>(); //key is TS, val=[cnt, ht]
        for(var event: buildings){//how to unpack array from Java?
            int st = event[0];
            int ed = event[1];
            int hh = event[2];

            long[] startVal = events.getOrDefault(st, new long[2]);
            long[] endVal = events.getOrDefault(ed, new long[2]);
            
            startVal[0] += 1;
            startVal[1] += hh;
            endVal[0] -= 1;
            endVal[1] -= hh;

            events.put(st, startVal);
            events.put(ed, endVal);
        }

        //calculate segments of avg
        List<long[]> segments = new ArrayList<>();
        long currCnt=0;
        long currHt=0;
        for(Map.Entry<Integer, long[]> entry :events.entrySet()){
            int ts = entry.getKey();
            long[] diff = entry.getValue();
            currCnt += diff[0];
            currHt += diff[1];
            long avg = (currCnt==0)?0:currHt/currCnt;
            segments.add(new long[]{ts, avg});
        }

        //merge segments of same avg to res
        int ii=0;
        List<List<Integer>> res = new ArrayList<>();
        while(ii<segments.size()){
            long ts = segments.get(ii)[0];
            long avg = segments.get(ii)[1];

            if(avg==0){//skip avg zeros
                ii+=1;
                continue;
            }

            int st = (int)ts;
            int jj = ii;
            while(jj<segments.size() && avg == segments.get(jj)[1]) ++jj;
            res.add(Arrays.asList(st, (int)segments.get(jj)[0], (int)avg));
            ii=jj;
        }
        //return res as int array of arrays


        // return res.stream()
        //           // Maps each List<Integer> (segment) to a primitive int[] array
        //           .map(list -> new int[]{list.get(0), list.get(1), list.get(2)})
                  
        //           // Collects the stream of int[] arrays into the final int[][] array
        //           .toArray(int[][]::new);

        return res.stream()
          // Use flatMap/mapToInt to process the inner list
          .map(list -> list.stream()
                           .mapToInt(Integer::intValue) // Unboxes and creates IntStream
                           .toArray())                  // Collects IntStream into int[]
          .toArray(int[][]::new);


    }
}

// ### Given
// * buildings=[[st, ed, h],...]
//     xxxxxx    
//  xxxxx
// xxx     xxxxx xxxx
// -------------------

// ### The ask
// hhhhhhhhhhhhh hhhh. < output intervals with same avg hight

// ### Analysis
// * N=10^5

// ##### bruteforce 
// * for each interval record [height, cnt] for all index in the range -> N^2

// ##### NlogN
// * intervals -> sweepline
// * DP



