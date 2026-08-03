from collections import deque
from typing import List


class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str],
    ) -> int:
        unvisited = set(wordList)

        if endWord not in unvisited:
            return 0

        queue = deque([beginWord])
        unvisited.discard(beginWord)

        # The sequence already contains beginWord.
        sequence_length = 1

        while queue:
            # Process one complete BFS level.
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return sequence_length

                chars = list(word)

                for i in range(len(chars)):
                    original_char = chars[i]

                    for code in range(ord("a"), ord("z") + 1):
                        new_char = chr(code)

                        if new_char == original_char:
                            continue

                        chars[i] = new_char
                        candidate = "".join(chars)

                        if candidate in unvisited:
                            # Mark visited when enqueueing.
                            unvisited.remove(candidate)
                            queue.append(candidate)

                    chars[i] = original_char

            sequence_length += 1

        return 0