class Solution {
    private int dfs(int idx, Map<Integer, Integer> idx2cntMemo, int D, int[] arr){
        int N=arr.length;
        if(idx2cntMemo.containsKey(idx)) return idx2cntMemo.get(idx);

        int res=1;//default is itself.
        //jumping left
        for(int jj=idx-1; jj>=Math.max(0, idx-D); --jj){
            if(arr[jj] >= arr[idx]) break;
            res=Math.max(res, 1+dfs(jj, idx2cntMemo, D, arr));
        }

        //jumping right
        for(int jj=idx+1; jj<Math.min(N, idx+D+1); ++jj){
            if(arr[jj] >= arr[idx]) break;
            res=Math.max(res, 1+dfs(jj, idx2cntMemo, D, arr));
        }

        idx2cntMemo.put(idx, res);
        return res;

    }
    public int maxJumps(int[] arr, int d) {
        int N=arr.length;

        Map<Integer, Integer> idx2cntMemo = new HashMap<>();

        //we need to try each index 
        int res=0;
        for(int ii=0; ii<N; ++ii){
            res=Math.max(res, dfs(ii, idx2cntMemo, d, arr));
        }

        return res;
    }
}