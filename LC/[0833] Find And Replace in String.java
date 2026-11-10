class Solution {
    public String findReplaceString(
            String s, int[] indices, String[] sources, String[] targets) {

        Integer[] order = new Integer[indices.length];
        for (int i = 0; i < order.length; i++) {
            order[i] = i;
        }

        // Sort operations by their starting positions.
        java.util.Arrays.sort(
                order, (a, b) -> Integer.compare(indices[a], indices[b]));

        StringBuilder result = new StringBuilder();
        int cursor = 0;

        for (int operation : order) {
            int index = indices[operation];
            String source = sources[operation];

            // Check against the original string.
            if (s.startsWith(source, index)) {
                result.append(s, cursor, index);
                result.append(targets[operation]);
                cursor = index + source.length();
            }
        }

        result.append(s, cursor, s.length());
        return result.toString();
    }
}