import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Map;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        Map<Character, Character> left2right = Map.of(
            '{', '}',
            '[', ']',
            '(', ')'
        );

        for (char cc : s.toCharArray()) {
            if (left2right.containsKey(cc)) {
                stack.push(cc);
            } else {
                if (stack.isEmpty() || cc != left2right.get(stack.peek())) {
                    return false;
                }
                stack.pop();
            }
        }

        return stack.isEmpty();
    }
}   