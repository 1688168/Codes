import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int ladderLength(
        String beginWord,
        String endWord,
        List<String> wordList
    ) {
        Set<String> validWords = new HashSet<>(wordList);

        if (!validWords.contains(endWord)) {
            return 0;
        }

        Set<Character> validChars = new HashSet<>();

        for (String word : validWords) {
            for (char ch : word.toCharArray()) {
                validChars.add(ch);
            }
        }

        Deque<String> queue = new ArrayDeque<>();
        queue.offer(beginWord);

        // Removing a word marks it as visited.
        validWords.remove(beginWord);

        int level = 0;

        while (!queue.isEmpty()) {
            level++;
            int levelSize = queue.size();

            for (int count = 0; count < levelSize; count++) {
                String word = queue.poll();

                if (word.equals(endWord)) {
                    return level;
                }

                char[] chars = word.toCharArray();

                for (int i = 0; i < chars.length; i++) {
                    char originalChar = chars[i];

                    for (char newChar : validChars) {
                        if (newChar == originalChar) {
                            continue;
                        }

                        chars[i] = newChar;
                        String newWord = new String(chars);

                        if (!validWords.contains(newWord)) {
                            continue;
                        }

                        // Mark as visited immediately.
                        validWords.remove(newWord);
                        queue.offer(newWord);
                    }

                    // Restore the original character.
                    chars[i] = originalChar;
                }
            }
        }

        return 0;
    }
}