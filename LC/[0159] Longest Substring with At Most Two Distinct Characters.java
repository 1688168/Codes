class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int N = s.length();
        int ll=0;
        Map<Character, Integer> charToCount = new HashMap<>();
        int mxl=0;
        for(int rr=0; rr<N; ++rr){
            char cc = s.charAt(rr);
            charToCount.put(cc, charToCount.getOrDefault(cc, 0)+1);

            while(charToCount.size() > 2){
                char leaving_char = s.charAt(ll);
                charToCount.put(leaving_char, charToCount.get(leaving_char)-1);
                if(charToCount.get(leaving_char)==0) charToCount.remove(leaving_char);
                ++ll;
            }
            mxl=Math.max(mxl, rr-ll+1);
        }        
        return mxl;
    }
}