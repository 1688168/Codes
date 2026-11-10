from typing import List

class Solution:
    def findReplaceString(
        self,
        s: str,
        indices: List[int],
        sources: List[str],
        targets: List[str],
    ) -> str:
        result = []
        cursor = 0

        operations = sorted(zip(indices, sources, targets))

        for index, source, target in operations:
            if s.startswith(source, index):
                result.append(s[cursor:index])
                result.append(target)
                cursor = index + len(source)

        result.append(s[cursor:])
        return "".join(result)