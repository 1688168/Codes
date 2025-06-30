class Solution {
    public int minCost(int[][] costs) {
        int N = costs.length;//num of houses 
        var costAtColor = new int[3];//where 0:cost of R, 1: cost of G, 2: cost of B @ current index
        costAtColor[0]=costs[0][0];
        costAtColor[1]=costs[0][1];
        costAtColor[2]=costs[0][2];

        for(int ii=1; ii<N; ++ii){
            var tmpCostAtColor = costAtColor.clone();
            costAtColor[0] = costs[ii][0] + Math.min(tmpCostAtColor[1], tmpCostAtColor[2]);
            costAtColor[1] = costs[ii][1] + Math.min(tmpCostAtColor[0], tmpCostAtColor[2]);
            costAtColor[2] = costs[ii][2] + Math.min(tmpCostAtColor[0], tmpCostAtColor[1]);
        }
        var ans = Arrays.stream(costAtColor).min().orElseThrow();
        return ans;
    }
}


// * N: num of houses (100) -> N^3
// * each house 3 color options: R, B, G
// * costs
// * constrain: adjacent house in diff color
// -> min cost to paint all houses0