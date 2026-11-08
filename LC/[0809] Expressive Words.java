class Solution {
    private Map<Character, Integer> s_map;

    private boolean isStretchy(String s, String ww, Map<Character, Integer> mm){
        boolean isStretchy = false;

        int ii=0;
        int jj=0;

        while(ii < s.length() && jj < ww.length()){

            if(s.charAt(ii) != ww.charAt(jj)) return false;

            int sCount=1;
            int wCount=1;
            while(ii<s.length()-1 && s.charAt(ii)==s.charAt(ii+1)){
                ++sCount;
                ++ii;
            }

            while(jj<ww.length()-1 && ww.charAt(jj)==ww.charAt(jj+1)){
                ++wCount;
                ++jj;
            } 
            if(wCount > sCount) return false;
            if(sCount > wCount && sCount < 3) return false;

            ++ii;
            ++jj;
        }

        isStretchy = (ii==s.length() && jj==ww.length());

        return isStretchy;
    }
    public int expressiveWords(String s, String[] words) {
        int count=0;
        s_map = new HashMap<>();
        for(var cc: s.toCharArray()){
            s_map.put(cc, s_map.getOrDefault(cc, 0)+1);
        }

        for(var ww :words){//100
            if(isStretchy(s, ww, s_map)) ++count;
        }

        return count;
    }
}