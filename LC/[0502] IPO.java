class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        List<int[]> capitalProfitList = new ArrayList<>();
        int N = profits.length;
        for(int ii=0; ii<N; ++ii){
            capitalProfitList.add(new int[]{capital[ii], profits[ii]});
        }

        int[][] capitalProfitSorted = capitalProfitList.stream().sorted(Comparator.comparingInt(cp -> cp[0])).toArray(int[][]::new);

        PriorityQueue<Integer> mxq = new PriorityQueue<>(Comparator.reverseOrder());

        int ii = 0;
        int cnt = 0;
        while(cnt < k) {
            while (ii < N && capitalProfitSorted[ii][0] <= w) {
                mxq.offer(capitalProfitSorted[ii][1]);
                ++ii;
            }

            if (mxq.isEmpty()) {
                break;
            }

            w += mxq.poll();
            ++cnt;
}

        return w;
    }
}