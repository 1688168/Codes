    /* why is this a fast slow pattern?
    * --> anytime you are checking existance of cycle
    * 1. no cycle -> ending @ 1
    * 2. going in cycle -> fast pointer will catch up the slow pointer
    */
        
class Solution {
    private int process(int nn){
        int ttl=0;
        while(nn > 0){
            int dd=nn%10;
            ttl += (dd*dd);
            nn/=10;
        }
        return ttl;
    }
    public boolean isHappy(int n) {
        //process digit by digit
        int n1=n;//slow
        int n2=n;//fast
        while(1==1){
            //process n1 for one pass
            n1 = process(n1);

            //process n2 for two pass
            n2 = process(n2);
            n2 = process(n2);
            if(n1==1 || n2==1) return true;
            if(n1==n2) break;
            //if any of the process reach 1 -> return true
            //if n1==n2 -> return False
        }
        return false;
    }
}