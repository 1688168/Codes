class Solution {
    public int lengthOfLongestSubstring(String s) {
        int N = s.length(); //take java string length
        Map<Character, Integer> char2Cnt = new HashMap<>();
        int left=0;
        int max_width=0;
        for(int right=0; right<N; ++right){
            char cc = s.charAt(right);
            char2Cnt.put(cc, char2Cnt.getOrDefault(cc, 0) + 1); //getOrDefault vs computIfAbsent
            while(right-left+1 > char2Cnt.size() && left <= right){ //we have duplicates
                char2Cnt.put(s.charAt(left), char2Cnt.get(s.charAt(left))-1);
                if(char2Cnt.get(s.charAt(left))==0) char2Cnt.remove(s.charAt(left)); //need to remove if zero
                ++left;
            }

            max_width = Math.max(max_width, char2Cnt.size());
        }
        return max_width;
    }
}