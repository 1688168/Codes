class Solution {
    private String multiplyByOneDigit(String num, int digit){
        int carry=0;
        StringBuilder res_rev = new StringBuilder();
        for(int ii=0; ii<num.length(); ++ii){
            int curr = num.charAt(ii) - '0';
            int total = curr*digit+carry;
            res_rev.append(total%10);
            carry = total/10;

        }
        if(carry > 0) res_rev.append(carry);
        
        return res_rev.toString();
    }

    private String addTwoNum(String num1_rev, String num2_rev){
        int ii=0;
        int jj=0;
        int carry=0;
        StringBuilder res_rev = new StringBuilder();
        while(ii<num1_rev.length() && jj < num2_rev.length()){
            int d1 = num1_rev.charAt(ii) - '0';
            int d2 = num2_rev.charAt(jj) - '0';
            int total = d1+d2+carry;
            res_rev.append(total%10);
            carry = total/10;
            ++ii;
            ++jj;
        }

        while(ii < num1_rev.length()){
            int total = num1_rev.charAt(ii) - '0' + carry;
            res_rev.append(total%10);
            carry = total/10;
            ++ii;
        }

        while(jj < num2_rev.length()){
            int total = num2_rev.charAt(jj) - '0' + carry;
            res_rev.append(total%10);
            carry = total/10;
            ++jj;
        }

        if(carry > 0) res_rev.append(carry);

        return res_rev.toString();
    }

    public String multiply(String num1, String num2) {
        if(num1.equals("0") || num2.equals("0")) return "0";
        if(num1.length() < num2.length()){
            String tmp=num1;
            num1=num2;
            num2=tmp;
        }

        //reverse both num
        String num1_rev = new StringBuilder(num1).reverse().toString();
        String num2_rev = new StringBuilder(num2).reverse().toString();

        //multiply num1_rev by num2_rev digit by digit
        StringBuilder zero = new StringBuilder();
        String res_rev="";
        for(int ii=0; ii<num2_rev.length(); ++ii){
            int digit = num2_rev.charAt(ii) - '0';
            if(digit!=0){
                String product_rev = multiplyByOneDigit(num1_rev, digit);
                product_rev = zero.toString() + product_rev;
                res_rev = addTwoNum(res_rev, product_rev);
            }
            zero.append('0');
        }

        return new StringBuilder(res_rev).reverse().toString();
    }
}