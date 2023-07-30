class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        sweep_lines=[]

        for n in nums:
            sweep_lines.append((n-k, True))
            sweep_lines.append((n+k+1, False))
        
        sweep_lines.sort()

        cnt, mx_cnt=0, 0
        for n, is_start in sweep_lines:
            if is_start:
                cnt +=1
            else:
                cnt -= 1
            mx_cnt=max(mx_cnt, cnt)


        return mx_cnt

        


