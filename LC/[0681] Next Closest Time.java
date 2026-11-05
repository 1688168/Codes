import java.util.HashSet;
import java.util.Locale;
import java.util.Set;

class Solution {
    public String nextClosestTime(String time) {
        int hour = Integer.parseInt(time.substring(0, 2)); //java:  substring, convert string to int
        int minute = Integer.parseInt(time.substring(3, 5));

        Set<Character> allowed = new HashSet<>();
        for (char ch : time.toCharArray()) {
            allowed.add(ch);
        }

        while (true) {
            minute++;
            if (minute == 60) {
                minute = 0;
                hour = (hour + 1) % 24;
            }

            String candidate = String.format(Locale.ROOT, "%02d:%02d", hour, minute);//java string format
            boolean valid = true;

            for (char ch : candidate.toCharArray()) {
                if (!allowed.contains(ch)) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                return candidate;
            }
        }
    }
}