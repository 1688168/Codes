import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean backspaceCompare(String s, String t) {
        return typedChars(s).equals(typedChars(t));
    }

    private List<Character> typedChars(String text) {
        List<Character> stack = new ArrayList<>();

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);

            if (c == '#') {
                if (!stack.isEmpty()) {
                    stack.remove(stack.size() - 1);
                }
            } else {
                stack.add(c);
            }
        }

        return stack;
    }
}