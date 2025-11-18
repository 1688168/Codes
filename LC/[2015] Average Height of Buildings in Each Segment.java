import java.util.*;

class Solution {
    public int[][] averageHeightOfBuildings(int[][] buildings) {
        
        // 1. Collect events
        // Use a TreeMap to keep the keys (timestamps) sorted automatically.
        // The value is an array [diffCount, diffHeight].
        // We use 'long' to prevent overflow during accumulation.
        Map<Integer, long[]> events = new TreeMap<>();//java sorted map.
        
        for (int[] building : buildings) {//
            int st = building[0];
            int ed = building[1];
            int ht = building[2];
            
            //starting event
            // Add height and count at the start position
            long[] startVal = events.getOrDefault(st, new long[2]);//java map default value
            startVal[0] += 1;//cnt
            startVal[1] += ht;//measure
            events.put(st, startVal);//add element to map. key=ts, value=[cnt, measure]
            
            //ending event
            // Subtract height and count at the end position
            long[] endVal = events.getOrDefault(ed, new long[2]);
            endVal[0] -= 1;
            endVal[1] -= ht;
            events.put(ed, endVal);
        }

        // 2. Calculate segments with average heights
        // This list will store pairs of [timestamp, average_height]
        List<long[]> segments = new ArrayList<>();
        long currCnt = 0;
        long currHt = 0;
        
        // Iterate through the sorted events (TreeMap handles sorting)
        for (Map.Entry<Integer, long[]> entry : events.entrySet()) {//how to traverse map
            int ts = entry.getKey();
            long[] diff = entry.getValue();
            
            currCnt += diff[0];
            currHt += diff[1];
            
            long avg = (currCnt == 0) ? 0 : currHt / currCnt;
            segments.add(new long[]{ts, avg});
        }

        // 3. Merge segments with the same average height
        List<List<Integer>> res = new ArrayList<>();
        int ii = 0;
        
        while (ii < segments.size()) {
            long ts = segments.get(ii)[0];
            long avg = segments.get(ii)[1];

            // Skip segments with no buildings
            if (avg == 0) {
                ii++;
                continue;
            }
            
            int st = (int)ts;

            int jj = ii;
            // Find the end of this segment (where the avg changes)
            while (jj < segments.size() && segments.get(jj)[1] == avg) {
                jj++;
            }
            
            // The segment ends at the start of the *next* segment
            int ed = (int)segments.get(jj)[0];
            
            // Add the merged segment [start, end, avg]
            res.add(Arrays.asList(st, ed, (int)avg));//how to add 3 elements as list to a list
            
            // Move the pointer to the next segment
            ii = jj;
        }
        
        // 4. Convert the List<List<Integer>> to int[][] using streams
        // This is the updated, more concise conversion
        return res.stream()
                  .map(list -> new int[]{list.get(0), list.get(1), list.get(2)})
                  .toArray(int[][]::new);
    }
}