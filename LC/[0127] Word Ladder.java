import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;

class Solution {
    public int ladderLength(
        String beginWord,
        String endWord,
        List<String> wordList
    ) {
        Set<String> unvisited = new HashSet<>(wordList); 

        // endWord must appear in wordList.
        if (!unvisited.contains(endWord)) {
            return 0;
        }

        Queue<String> queue = new ArrayDeque<>();
        queue.offer(beginWord);

        // Mark beginWord visited if it appears in wordList.
        unvisited.remove(beginWord);

        // beginWord is the first word in the sequence.
        int sequenceLength = 1;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();

            // Process one complete BFS level.
            for (int count = 0; count < levelSize; count++) {
                String word = queue.poll();

                if (word.equals(endWord)) {
                    return sequenceLength;
                }

                char[] chars = word.toCharArray();

                for (int i = 0; i < chars.length; i++) {
                    char originalChar = chars[i];

                    for (char letter = 'a'; letter <= 'z'; letter++) {
                        if (letter == originalChar) {
                            continue;
                        }

                        chars[i] = letter;
                        String candidate = new String(chars);

                        if (unvisited.contains(candidate)) {
                            // Mark visited when enqueueing.
                            unvisited.remove(candidate);
                            queue.offer(candidate);
                        }
                    }

                    // Restore the original word before moving
                    // to the next character position.
                    chars[i] = originalChar;
                }
            }

            sequenceLength++;
        }

        return 0;
    }
}