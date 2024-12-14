class Solution {
    public int countPartitions(int[] nums, int k) {
        int N = nums.length;
        int M = (int) (1e9 + 7);

        //initial sanity check
        long sum = 0;
        for(var nn :nums) sum += nn; 

        if(sum < 2*k) return 0;

        //convert int array to Integer Array List
        List<Integer> list = IntStream.of(nums).boxed().collect(Collectors.toCollection(ArrayList::new));
        //insert dummy in the beginning of nums
        list.add(0, 0); //java insert dummy in the beginning of nums

        //two dimential arrayList
        List<List<Integer>> dp = new ArrayList<>();   
        for(int ii=0; ii<=N; ++ii) dp.add(new ArrayList<Integer>(Collections.nCopies(k, 0)));

        //initialize DP: set dp[0][0]=1
        dp.get(0).set(0, 1);

        //start populate DP
        for(int ii=1; ii<=N; ++ii){//for each project: 0 is dummy, 1~N (1~4)
            for(int jj=0; jj<k; ++jj){ //for each invalid outcome space (sum(A)) (0~k-1)=(0~3)
                //skip
                dp.get(ii).set(jj, (dp.get(ii).get(jj) + dp.get(ii-1).get(jj))%M);
             
                //take
                if(jj >= list.get(ii)) dp.get(ii).set(jj, 
                (dp.get(ii).get(jj) + dp.get(ii-1).get(jj-list.get(ii)))%M);
            }
        }

        int invalid = 0;
     
        for(int kk=0; kk< k; ++kk) invalid = (invalid + dp.get(N).get(kk))%M;
        System.out.println("Invalid: " + invalid);

        int ttl=1;
        for(int ii=0; ii < N; ++ii) ttl = (ttl*2)%M;

        return (ttl-2*invalid+M)%M;
    }
}