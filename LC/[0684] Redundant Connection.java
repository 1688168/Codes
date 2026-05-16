class Solution {
    private Map<Integer, Integer> parent = new HashMap<>();

    public int[] findRedundantConnection(int[][] edges) {
        for (int[] edge : edges) {
            int a = edge[0];
            int b = edge[1];

            if (!parent.containsKey(a)) parent.put(a, a);
            if (!parent.containsKey(b)) parent.put(b, b);

            if (find(a) == find(b)) {
                return edge;
            }

            union(a, b);
        }

        return new int[0];
    }

    private int find(int x) {
        if (parent.get(x) != x) {
            parent.put(x, find(parent.get(x)));
        }
        return parent.get(x);
    }

    private void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x == y) return;

        if (x < y) {
            parent.put(y, x);
        } else {
            parent.put(x, y);
        }
    }
}