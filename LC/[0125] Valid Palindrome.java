class Solution {
    public boolean isPalindrome(String s) {
        int N=s.length();
        int ll=0, rr=N-1;

        while(ll<rr){
            while(ll<rr && !Character.isLetterOrDigit(s.charAt(ll))) ++ll;
            while(rr>ll && !Character.isLetterOrDigit(s.charAt(rr))) --rr;
            if(Character.toLowerCase(s.charAt(ll)) != Character.toLowerCase(s.charAt(rr))) return false;
            ++ll;
            --rr;
        }
        return true;
    }
}