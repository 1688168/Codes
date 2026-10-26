class Solution:
    def multiply_one_digit(self, num: str, digit: int) -> str:
        result = []
        carry = 0

        for ch in reversed(num):
            total = int(ch) * digit + carry
            result.append(str(total % 10))
            carry = total // 10

        if carry:
            result.append(str(carry))

        return "".join(reversed(result))

    def add_strings(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry
            result.append(str(total % 10))
            carry = total // 10

            i -= 1
            j -= 1

        return "".join(reversed(result))

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Use the shorter number as the multiplier.
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        result = "0"

        for shift, ch in enumerate(reversed(num2)):
            if ch == "0":
                continue

            row = self.multiply_one_digit(num1, int(ch))
            row += "0" * shift
            result = self.add_strings(result, row)

        return result