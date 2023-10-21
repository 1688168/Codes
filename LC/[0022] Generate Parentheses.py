class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, path):
            if left <= 0 and right <= 0:  # successfully complete
                res.append(path)
                return

            if left > 0:
                dfs(left-1, right, path+"(")

            if left < right:
                dfs(left, right-1, path+")")

        dfs(n, n, "")  # both left, right need to consume n

        return res
