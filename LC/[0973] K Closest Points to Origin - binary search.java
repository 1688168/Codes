import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.LongSummaryStatistics;
import java.util.stream.IntStream;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // ArrayList<Long> dist = Arrays.stream(points)
        //     .map(point -> (long) point[0] * point[0]
        //                 + (long) point[1] * point[1])
        //     .collect(Collectors.toCollection(ArrayList::new));

        // long ll = 0;
        // long rr = dist.stream()
        //               .mapToLong(Long::longValue)
        //               .max()
        //               .getAsLong();

        ArrayList<Long> dist = Arrays.stream(points)
            .map(point -> (long) point[0] * point[0]
                        + (long) point[1] * point[1])
            .collect(Collectors.toCollection(ArrayList::new));

        LongSummaryStatistics stats = dist.stream()
            .mapToLong(Long::longValue)
            .summaryStatistics();

        long ll = stats.getMin();
        long rr = stats.getMax();              

        long ans = rr;

        while (ll <= rr) {
            long mm = ll + (rr - ll) / 2;

            if (count(dist, mm) >= k) {
                ans = mm;
                rr = mm - 1;
            } else {
                ll = mm + 1;
            }
        }

        // ArrayList<int[]> result = new ArrayList<>();

        // for (int i = 0; i < points.length && result.size() < k; i++) {
        //     if (dist.get(i) <= ans) {
        //         result.add(points[i]);
        //     }
        // }

        final long threshold = ans;

        // return IntStream.range(0, points.length)
        //     .filter(i -> dist.get(i) <= threshold)
        //     .limit(k)
        //     .mapToObj(i -> points[i])
        //     .toArray(int[][]::new);

        ArrayList<int[]> result = new ArrayList<>();

        for (int i = 0; i < points.length; i++) {
            if (dist.get(i) < threshold) {
                result.add(points[i]);
            }
        }

        for (int i = 0; i < points.length && result.size() < k; i++) {
            if (dist.get(i) == threshold) {
                result.add(points[i]);
            }
        }

        return result.toArray(new int[0][]);


    }

    private int count(ArrayList<Long> dist, long threshold) {
        int cnt = 0;

        for (long dd : dist) {
            if (dd <= threshold) {
                cnt++;
            }
        }

        return cnt;
    }
}