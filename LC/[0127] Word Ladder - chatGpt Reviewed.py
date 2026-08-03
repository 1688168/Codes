from collections import defaultdict, deque
from string import ascii_lowercase
from typing import List


class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str],
    ) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        word_set.add(beginWord)

        # Build the graph.
        graph = defaultdict(set)

        for word in word_set:
            for i in range(len(word)):
                for char in ascii_lowercase:
                    if char == word[i]:
                        continue

                    candidate = word[:i] + char + word[i + 1:]

                    if candidate in word_set:
                        graph[word].add(candidate)

        # Level-order BFS.
        queue = deque([beginWord])
        visited = {beginWord}
        sequence_length = 1

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                word = queue.popleft()

                if word == endWord:
                    return sequence_length

                for neighbor in graph[word]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            sequence_length += 1

        return 0