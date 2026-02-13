import java.util.*;

class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        // x -> list of (height, flag) where flag=+1 start, flag=-1 end
        TreeMap<Integer, List<int[]>> events = new TreeMap<>();

        for (int[] b : buildings) {
            int L = b[0], R = b[1], H = b[2];
            events.computeIfAbsent(L, k -> new ArrayList<>()).add(new int[]{H, 1});   // start
            events.computeIfAbsent(R, k -> new ArrayList<>()).add(new int[]{H, -1}); // end
        }

        // Java doesn't have multiset; use TreeMap<height, count> as a multiset.
        TreeMap<Integer, Integer> multiset = new TreeMap<>();
        List<List<Integer>> res = new ArrayList<>();

        for (Map.Entry<Integer, List<int[]>> entry : events.entrySet()) {
            int x = entry.getKey();
            List<int[]> list = entry.getValue();

            // apply all events at this x
            for (int[] e : list) {
                int h = e[0], flag = e[1];
                if (flag == 1) {
                    multiset.put(h, multiset.getOrDefault(h, 0) + 1);
                } else {
                    int cnt = multiset.getOrDefault(h, 0);
                    if (cnt <= 1) multiset.remove(h);
                    else multiset.put(h, cnt - 1);
                }
            }

            // current max height
            int currH = multiset.isEmpty() ? 0 : multiset.lastKey();

            // append key point if height changes
            if (res.isEmpty() || !res.get(res.size() - 1).get(1).equals(currH)) {
                res.add(Arrays.asList(x, currH));
            }
        }

        return res;
    }
}