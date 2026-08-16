import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public String decodeString(String s) {
        // Mental model: curr_str + curr_cnt * next

        StringBuilder currStr = new StringBuilder();
        int currNum = 0;

        Deque<String> stringStack = new ArrayDeque<>();//java stack is using Deque
        Deque<Integer> numberStack = new ArrayDeque<>();

        for (char cc : s.toCharArray()) {//converting String to charArray
            if (Character.isDigit(cc)) {//how to check if char is digit
                // Accumulate multi-digit numbers
                currNum = currNum * 10 + (cc - '0');//how to convert char to num in Java

            } else if (cc == '[') {
                // Save the current context
                stringStack.push(currStr.toString());
                numberStack.push(currNum);

                currStr = new StringBuilder();
                currNum = 0;

            } else if (cc == ']') {
                // Restore the previous context
                String previousString = stringStack.pop();
                int repeatCount = numberStack.pop();

                String decodedSection = currStr.toString();//convert string builder to string
                currStr = new StringBuilder(previousString);

                for (int i = 0; i < repeatCount; i++) {//how to repeat and append string
                    currStr.append(decodedSection);
                }

            } else {
                // Regular character
                currStr.append(cc);
            }
        }

        return currStr.toString();//from string builder to string
    }
}