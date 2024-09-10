class Solution {
    /*
    Problem: given a list of stones, cancel/merge any two until only one or none last.
    Asking: the remaining weight after all cancel/merge
    Observation: eventually the cancel/merge process can be represented as: 
    -> ((B-A)-C)-(D-E))
    -> flattening
    -> B-A-C-D+E
    -> (B+E)  -  (C+D)
       bigger     smaller
    => partition to two groups. 
    => sum(bigger)-sum(smaller) ~= 0 
    => sum(smaller) <= total/2
    => knapsack problem: pick/skip element to smaller_group with capacity=total//2
    => dp[ii][jj] = max total weight for smaller group using up to iith stone with capacity jj
    => return total-2*dp[-1][capacity]

    # Solution II:
    * bigger-smaller
    = subsetA-subsetB
    = a+b+c+...-x-y-z

    -> we will have each element being assigned with + or -
    -> if we can construct all potential result and return the smallest one that is greater than equal to zero
    */
    public int lastStoneWeightII(int[] stones) {
        Set<Integer> set = new HashSet<>();
        set.add(0);

        for(var ss :stones){//for each stone
            Set<Integer> sset = new HashSet(set);
            set.clear();
            //collecting all possible final combination
            for(var s: sset){//for each final num.
                set.add(s+Integer.valueOf(ss));
                set.add(s-Integer.valueOf(ss));
            }
        }
        //System.out.println(set);
        //find the smallest final combination that is >=0
        int ans=Integer.MAX_VALUE;
        for(var x: set){
            ans = (x >=0 && x<ans)? x:ans;
        }
        return ans;
    }
}