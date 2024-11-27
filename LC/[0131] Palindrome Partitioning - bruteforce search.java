/*
* *return all possible results -> search for all
* * 
*/

class Solution {
    private List<List<String>> res = new ArrayList<List<String>>();//java two dimensional ArrayList
    private Boolean isPalindrome(String ss){
        int ii=0, jj=ss.length()-1;
        //System.out.println(ss);
        if(ii==jj) return true;

        while(ii<jj){
            if(ss.charAt(ii) != ss.charAt(jj)) return false;
            ++ii;
            --jj;
        }
        return true;
    }

    private void partition(String s, int st, List<String> path){
        int N = s.length();
        if(st>=N){
            res.add(path);
            return;
        }

        for(int ii=st; ii<N; ++ii){
            String ss=s.substring(st, ii+1);
            if(isPalindrome(ss)){
                //java concatenate two lists
                partition(s, ii+1, Stream.concat(path.stream(),List.of(ss).stream()).collect(Collectors.toList()));
            }
        }

        return;
    }
    public List<List<String>> partition(String s) {
        
        List<String> path = new ArrayList<String>();
        partition(s, 0, path);
        
        return res;
    }
}