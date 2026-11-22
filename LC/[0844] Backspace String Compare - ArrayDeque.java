import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Iterator;

class Solution {
    public boolean backspaceCompare(String s, String t) {
        Deque<Character> left = typedChars(s);
        Deque<Character> right = typedChars(t);

        if (left.size() != right.size()) {
            return false;
        }

        Iterator<Character> a = left.iterator();
        Iterator<Character> b = right.iterator();

        while (a.hasNext()) {
            if (!a.next().equals(b.next())) {
                return false;
            }
        }

        return true;
    }

    private Deque<Character> typedChars(String text) {
        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c == '#') {
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else {
                stack.push(c);
            }
        }

        return stack;
    }
}