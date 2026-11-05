class Solution {
    public String nextClosestTime(String time) {
        char[] current = {
            time.charAt(0), time.charAt(1),
            time.charAt(3), time.charAt(4)
        };

        boolean[] allowed = new boolean[10];
        char smallest = '9';
        for (char digit : current) {
            allowed[digit - '0'] = true;
            if (digit < smallest) {
                smallest = digit;
            }
        }

        char[] candidate = current.clone();
        for (int i = candidate.length - 1; i >= 0; i--) {
            for (int digit = current[i] - '0' + 1; digit < 10; digit++) {
                if (!allowed[digit]) {
                    continue;
                }

                candidate[i] = (char) ('0' + digit);
                int hour = 10 * (candidate[0] - '0') + (candidate[1] - '0');
                int minute = 10 * (candidate[2] - '0') + (candidate[3] - '0');

                if (hour < 24 && minute < 60) {
                    return new String(candidate, 0, 2) + ":"
                         + new String(candidate, 2, 2);
                }
            }

            candidate[i] = smallest;
        }

        return new String(candidate, 0, 2) + ":"
             + new String(candidate, 2, 2);
    }
}