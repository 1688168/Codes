class Solution {
    public List<List<Long>> splitPainting(int[][] segments) {

        // TreeMap = ordered map (same as C++ map)
        TreeMap<Long, Long> events = new TreeMap<>();

        for (int[] seg : segments) {
            long l = seg[0], r = seg[1], c = seg[2];
            events.put(l, events.getOrDefault(l, 0L) + c);
            events.put(r, events.getOrDefault(r, 0L) - c);
        }

        List<List<Long>> rets = new ArrayList<>();
        long cnt = 0;
        long start = -1, end = -1;

        for (Map.Entry<Long, Long> event : events.entrySet()) {
            long pos = event.getKey();
            long diff = event.getValue();

            if (start == -1) {
                start = pos;
            } else {
                end = pos;

                rets.add(Arrays.asList(start, end, cnt));

                start = end;
            }

            cnt += diff;

            if (cnt == 0) start = -1;
        }

        return rets;
    }
}