class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_number = 0

        for char in s:
            if char.isdigit():
                # Handles multi-digit numbers such as 12[a]
                current_number = current_number * 10 + int(char)

            elif char == "[":
                # Save the outer context
                stack.append((current_string, current_number))

                # Start decoding the bracket contents
                current_string = ""
                current_number = 0

            elif char == "]":
                previous_string, repeat_count = stack.pop()

                current_string = (
                    previous_string
                    + current_string * repeat_count
                )

            else:
                current_string += char

        return current_string