class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        start = "0" * (n - 1)
        used = set()
        reverse_labels = []

        def dfs(suffix: str) -> None:
            for digit in map(str, range(k)):
                password = suffix + digit
                if password in used:
                    continue

                used.add(password)
                next_suffix = password[1:]
                dfs(next_suffix)
                reverse_labels.append(digit)

        dfs(start)
        return start + "".join(reversed(reverse_labels))
