class Solution {
    public int trap(int[] height) {
        Deque<Integer> stack = new ArrayDeque<>();

        int N = height.length;

        int ans=0;
        for(int ii=0; ii<N; ++ii){
            int hh=height[ii];
            while(!stack.isEmpty() && hh >= height[stack.peek()]){
                int hh_base = height[stack.poll()];
                if(!stack.isEmpty()){
                    int dist=ii-stack.peek()-1;
                    ans += (Math.min(hh, height[stack.peek()])-hh_base)*dist;
                }
            }
            stack.push(ii);
        }

        return ans;
    }
}