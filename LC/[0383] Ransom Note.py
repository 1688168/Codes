class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char2cnt = {}
        for c in magazine:
            char2cnt[c] = char2cnt.get(c, 0) + 1

        for c in ransomNote:
            if c not in char2cnt:
                return False
            char2cnt[c] -= 1
            if char2cnt[c] == 0:
                del char2cnt[c]

        return True
