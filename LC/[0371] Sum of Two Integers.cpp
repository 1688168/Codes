class Solution {
public:
    int getSum(int a, int b) {
            while(b != 0){
                unsigned tmpA=a;
                a ^= b;
                b = (tmpA&b) <<1;


            }
        return a;

            // while(b) {
            //     unsigned c = a&b;
            //     a ^= b;
            //     b = c << 1;
            // }
            // return a;
    }
};


### solution 2
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = abs(a)
        y = abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)

        # abs(a) >= abs(b) -->
        # a determines the sign
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        return x * sign
