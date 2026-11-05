class Solution:
    def nextClosestTime(self, time: str) -> str:
        current = time[:2] + time[3:]
        digits = sorted(set(current))
        smallest = digits[0]

        for index in range(3, -1, -1):
            for digit in digits:
                if digit <= current[index]:
                    continue

                candidate = (
                    current[:index] + digit + smallest * (3 - index)
                )
                if candidate[:2] < "24" and candidate[2:] < "60":
                    return f"{candidate[:2]}:{candidate[2:]}"

        return f"{smallest * 2}:{smallest * 2}"