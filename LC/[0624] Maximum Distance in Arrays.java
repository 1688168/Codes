class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        /*
        * consider bruteforce: for each min at each row, we need to calc dist vs each max on each row.
        * we cannot do diff for max/min on same row.  if we capture max_so_far, min_so_far and consider curr_min, curr_max from each row. we can calc max_dist so far.
        */
        int M=arrays.size();
        int min_so_far=arrays.get(0).get(0);
        int max_so_far=arrays.get(0).get(arrays.get(0).size()-1);
        int dist=0;
        for(int ii=1; ii<M; ++ii){//for each array  
            var curr_arr = arrays.get(ii);
            var curr_min=curr_arr.get(0);
            var curr_max=curr_arr.get(curr_arr.size()-1);
            dist = Math.max(dist, Math.abs(curr_max-min_so_far));
            dist = Math.max(dist, Math.abs(max_so_far-curr_min));
            min_so_far = Math.min(min_so_far, curr_min);
            max_so_far = Math.max(max_so_far, curr_max);
        }
        
        return dist;
    }
}


