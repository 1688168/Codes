class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup_count=0 # increment when a char increment to 2, decrement when a char decrement to 1
        char2count=defaultdict(int)

        left, right = 0, 0
        width=0 # s could be 0
        N=len(s)
        while right < N and left <= right:
            char2count[s[right]] += 1
            if char2count[s[right]] == 2: dup_count += 1

            while dup_count > 0 and left <= right: #shrink the window until we have no duplicate
                char2count[s[left]] -= 1
                if char2count[s[left]] == 1: dup_count -= 1
                left += 1

            width = max(width, right-left+1)            
            right += 1

        return width
