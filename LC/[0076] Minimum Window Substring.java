class Solution {
    public String minWindow(String s, String t) {
        //edge case
        //if s==t -> return s
        //if len(s) < len(t) -> return ""
        if(s.equals(t)) return s;
        if(s.length() < t.length()) return "";
        
        //A: expand right pointer until we have a substring in s that contains t
        //set up two pointers and data structure to manage the status

        Map<Character, Integer> required = new HashMap<>();
        //construct required from t
        int n=t.length();
        for(int ii=0; ii<n; ++ii){
            char cc = t.charAt(ii);
            required.put(cc, required.getOrDefault(cc, 0)+1);
        }

        //initialize contains
        Map<Character, Integer> contains = new HashMap<>(required);

        int m = s.length();
        int ll=0;
        int match_count=0;

        int mnl=Integer.MAX_VALUE;
        int best_start = 0;
        for(int rr=0; rr<m; ++rr){
            //isContained
            char cc = s.charAt(rr);
            contains.put(cc, contains.getOrDefault(cc,0)-1);
            if(required.containsKey(cc) && contains.get(cc)==0){
                ++match_count;
            }

            //B: shrink the substring by advancing the left pointer until the substring no longer. contains t -> repeat A
            while(ll<=rr && match_count == required.size()){
                if(rr-ll+1 < mnl){
                    mnl=rr-ll+1;
                    best_start=ll;
                }
                char leaving_char = s.charAt(ll);
                contains.put(leaving_char, contains.get(leaving_char)+1);
                if(required.containsKey(leaving_char) && contains.get(leaving_char)> 0){
                    --match_count;
                }
                ++ll;
            }
        }

        if(mnl==Integer.MAX_VALUE) return "";

        return s.substring(best_start, best_start + mnl);

    }
}

/*
* we want to know the shortest substring of s that contains t (case sensitive)

>  S contains T with shortest window -> two pointers
* 1. find a window contains T
* 2. can we shrink the window?

> How do we keep status of satisfied?
* if cc in required and contains drop to zero -> a match
* if match count same as requiredUniqueKey count -> we have a window contains t

> when we have a. window contains t -> try shrink the window (left pointer )and record the min_window until we no longer contains
> repeat expanding right pointer


*/