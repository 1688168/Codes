class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Changed: compare whole strings and expand the one-line statement.
        if num1 == "0" or num2 == "0":
            return "0"

        # Added: use the shorter number as the multiplier, reducing row additions.
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        # Renamed: make the reversed representation explicit.
        reversed_num1 = num1[::-1]
        reversed_num2 = num2[::-1]

        # Changed: descriptive parameter name and type annotations.
        def multiply_by_digit(reversed_num: str, digit: int) -> str:
            carry = 0
            digits = []  # Changed: append to a list, then join once.

            # Changed: iterate over characters directly; no index is needed.
            for char in reversed_num:
                # Changed: calculate product plus carry once.
                total = int(char) * digit + carry
                digits.append(str(total % 10))
                carry = total // 10

            if carry:  # Changed: idiomatic check for a nonzero carry.
                digits.append(str(carry))

            return "".join(digits)  # Changed: build the string once.

        # Renamed: describe the operation and the reversed inputs.
        def add_reversed(left: str, right: str) -> str:
            left_length = len(left)
            right_length = len(right)
            digits = []
            carry = 0  # Changed: initialize carry only once.

            for index in range(max(left_length, right_length)):
                left_digit = int(left[index]) if index < left_length else 0
                right_digit = int(right[index]) if index < right_length else 0

                # Fixed: use both guarded digits without indexing again.
                total = left_digit + right_digit + carry
                digits.append(str(total % 10))
                carry = total // 10

            if carry:
                digits.append(str(carry))

            return "".join(digits)

        result = "0"  # Changed: use a valid numeric string as the initial sum.

        # Changed: enumerate supplies both the shift and the character.
        for shift, char in enumerate(reversed_num2):
            if char == "0":  # Added: a zero row contributes nothing.
                continue

            partial_product = multiply_by_digit(reversed_num1, int(char))

            # Changed: apply the shift here, keeping addition independent.
            shifted_product = "0" * shift + partial_product
            result = add_reversed(result, shifted_product)

        return result[::-1].lstrip("0") or "0"