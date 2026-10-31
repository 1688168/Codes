class Solution {
    public int[] plusOne(int[] digits) {
        //reverse digits
        int ll=0, rr=digits.length-1;
        int N = digits.length;
        while(ll<rr){
            int tmp=digits[ll];
            digits[ll]=digits[rr];
            digits[rr]=tmp;
            ++ll;
            --rr;
        }

        int carry=0;
        for(int ii=0; ii<N; ++ii){
            int total = digits[ii]+carry;
            if(ii==0) total += 1;
            digits[ii] = total%10;
            carry = total/10;
        }
        int sz = carry > 0 ? 1: 0;
        int[] res = new int[N+sz];
        for(int ii=0; ii<N; ++ii) res[ii]=digits[ii];
        if(carry > 0) res[N]=carry;

        ll=0;
        rr=res.length-1;
        while(ll<rr){
            int tmp = res[ll];
            res[ll]=res[rr];
            res[rr]=tmp;
            ++ll;
            --rr;
        }

        return res;
    }
}