class Solution {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int N1=nums1.length;
        int N2=nums2.length;

        //java convert int array to ArrayList of Integer and insert dummy
        List<Integer> arr1 = Arrays.stream(nums1)
                                        .boxed()
                                        .collect(Collectors.toList());

        List<Integer> arr2 = Arrays.stream(nums2)
                                        .boxed()
                                        .collect(Collectors.toList());

        arr1.add(0, 0);//java insert dummy
        arr2.add(0, 0);

        //java convert arraylist back to int array
        nums1 = arr1.stream().mapToInt(Integer::intValue).toArray();
        nums2 = arr2.stream().mapToInt(Integer::intValue).toArray();



        var dp = IntStream.range(0, N1+1)
                          .mapToObj(ii->IntStream.range(0, N2+1)
                                        .map(jj->0).toArray()
                          ).toArray(int[][]::new);


        for(int ii=1; ii<=N1; ++ii){
            for(int jj=1; jj<=N2; ++jj){
                if(nums1[ii]==nums2[jj]){
                    dp[ii][jj]=dp[ii-1][jj-1]+1;
                }else{
                    dp[ii][jj] = Math.max(dp[ii-1][jj], dp[ii][jj-1]);
                }
            }
        }

        return dp[N1][N2];
    }
}