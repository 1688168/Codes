class Solution {

    private String multiplyByOneDigit(String numRev, int digit) {
        int carry = 0;
        StringBuilder resRev = new StringBuilder();

        for (int i = 0; i < numRev.length(); i++) {
            int number = numRev.charAt(i) - '0';
            int total = digit * number + carry;
            resRev.append(total % 10);
            carry = total / 10;
        }

        if (carry > 0) {
            resRev.append(carry);
        }

        return resRev.toString();
    }

    private String addTwoNums(String num1Rev, String num2Rev) {
        int n1 = num1Rev.length();
        int n2 = num2Rev.length();

        int i = 0;
        int j = 0;
        int carry = 0;
        StringBuilder res = new StringBuilder();

        while (i < n1 && j < n2) {
            int digit1 = num1Rev.charAt(i) - '0';
            int digit2 = num2Rev.charAt(j) - '0';
            int total = digit1 + digit2 + carry;

            res.append(total % 10);
            carry = total / 10;
            i++;
            j++;
        }

        while (i < n1) {
            int total = (num1Rev.charAt(i) - '0') + carry;
            res.append(total % 10);
            carry = total / 10;
            i++;
        }

        while (j < n2) {
            int total = (num2Rev.charAt(j) - '0') + carry;
            res.append(total % 10);
            carry = total / 10;
            j++;
        }

        if (carry > 0) {
            res.append(carry);
        }

        return res.toString();
    }

    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }

        String num1Rev = new StringBuilder(num1).reverse().toString();
        String num2Rev = new StringBuilder(num2).reverse().toString();

        if (num1Rev.length() < num2Rev.length()) {
            String temp = num1Rev;
            num1Rev = num2Rev;
            num2Rev = temp;
        }

        String res = "0";
        StringBuilder zeros = new StringBuilder();

        // Multiply the larger number by each digit of the smaller number.
        for (int scale = 0; scale < num2Rev.length(); scale++) {
            char digit = num2Rev.charAt(scale);

            if (digit != '0') {
                String productRev = multiplyByOneDigit(num1Rev, digit - '0');
                productRev = zeros.toString() + productRev;
                res = addTwoNums(res, productRev);
            }

            zeros.append('0');
        }

        return new StringBuilder(res).reverse().toString();
    }
}