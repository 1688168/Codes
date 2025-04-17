class Solution {
    public int minCost(int[][] costs) {
        int N=costs.length;
        int rr=costs[0][0];   
        int gg=costs[0][1];      
        int bb=costs[0][2];     

        for(int ii=1; ii<N; ++ii){
            int tmpRR=rr;
            int tmpGG=gg;
            int tmpBB=bb;
            rr=Math.min(tmpGG, tmpBB) + costs[ii][0];
            gg=Math.min(tmpRR, tmpBB) + costs[ii][1];
            bb=Math.min(tmpRR, tmpGG) + costs[ii][2];
        }

        int[] res = {rr, gg, bb};
        return IntStream.of(res)//[java][min][array]
                     .min()
                     .orElseThrow(() -> new RuntimeException("Array is empty"));

    }
}
/*
- N=100
- current state is make a decision out of 3 options.  the current decision cannot be the same as prev
- similar to house robber.  two options (rob/noRob). the current decision cannot be same as prev
-> min ttl cost
*/