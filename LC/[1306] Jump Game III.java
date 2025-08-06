class Solution {
    private boolean canReach(int[] arr, int start, Map<Integer, Integer> visited){
        int N = arr.length;
        if(start < 0 || start >= N) return false;
        if(visited.containsKey(start)) return false;
        if(arr[start]==0) return true;
        visited.put(start, 1);
        return canReach(arr, start-arr[start], visited) || canReach(arr, start+arr[start], visited);
    }
    public boolean canReach(int[] arr, int start) {
        HashMap<Integer, Integer> visited = new HashMap<>();
        return canReach(arr, start, visited);
    }
}

// * N=5*10^4 -> (N*50)*20
// * Can reach N-1 -> greedy -> O(N)
// * start at any and can reach any -> N^2 (x)
// * can you reach some index with value zero?
// * search all and reutrn true if found
// * otherwise return false @ the end