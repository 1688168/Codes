class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stk = []
        ans = [0]*n
        # print("logs: ", logs)
        # print(" ans: ", ans)
        for log in logs:
            idx, direction, ts = log.split(":")
            idx = int(idx)
            ts = int(ts)
            if direction == 'end':
                ts0, fii = stk.pop()
                print(stk)
                ans[idx] += (ts-ts0+1)

                if stk:
                    ans[stk[-1][1]] -= (ts-ts0+1)
            else:
                stk.append((ts, idx))

        return ans
