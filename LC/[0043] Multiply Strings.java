class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }

        // Use the shorter number as the multiplier.
        if (num1.length() < num2.length()) {
            String temp = num1;
            num1 = num2;
            num2 = temp;
        }

        String reversedNum1 = new StringBuilder(num1).reverse().toString();
        String reversedNum2 = new StringBuilder(num2).reverse().toString();

        String result = "0";
        StringBuilder shiftZeros = new StringBuilder();

        for (int shift = 0; shift < reversedNum2.length(); shift++) {
            char current = reversedNum2.charAt(shift);

            if (current != '0') {
                String partialProduct =
                        multiplyByDigit(reversedNum1, current - '0');

                // Leading zeros in reversed form apply the place-value shift.
                String shiftedProduct = shiftZeros.toString() + partialProduct;
                result = addReversed(result, shiftedProduct);
            }

            shiftZeros.append('0');
        }

        String product = new StringBuilder(result).reverse().toString();

        int start = 0;
        while (start < product.length() - 1 && product.charAt(start) == '0') {
            start++;
        }

        return product.substring(start);
    }

    private String multiplyByDigit(String reversedNum, int digit) {
        int carry = 0;
        StringBuilder digits = new StringBuilder();

        for (int index = 0; index < reversedNum.length(); index++) {
            int total = (reversedNum.charAt(index) - '0') * digit + carry;
            digits.append(total % 10);
            carry = total / 10;
        }

        if (carry != 0) {
            digits.append(carry);
        }

        return digits.toString();
    }

    private String addReversed(String left, String right) {
        int leftLength = left.length();
        int rightLength = right.length();
        int carry = 0;
        StringBuilder digits = new StringBuilder();

        for (int index = 0; index < Math.max(leftLength, rightLength); index++) {
            int leftDigit = index < leftLength ? left.charAt(index) - '0' : 0;
            int rightDigit = index < rightLength ? right.charAt(index) - '0' : 0;

            int total = leftDigit + rightDigit + carry;
            digits.append(total % 10);
            carry = total / 10;
        }

        if (carry != 0) {
            digits.append(carry);
        }

        return digits.toString();
    }
}