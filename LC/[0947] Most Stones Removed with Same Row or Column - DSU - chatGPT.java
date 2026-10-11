import java.util.*;

class DSU {
    private Map<Integer, Integer> parents;
    private Map<Integer, Integer> node2size;

    DSU() {
        parents = new HashMap<>();
        node2size = new HashMap<>();
    }

    public int find(int xx) {
        // Lazy initialization
        if (!parents.containsKey(xx)) {
            parents.put(xx, xx);
            node2size.put(xx, 1);
        }

        // Path compression
        if (xx != parents.get(xx)) {
            parents.put(xx, find(parents.get(xx)));
        }

        return parents.get(xx);
    }

    public void union(int aa, int bb) {
        int pa = find(aa);
        int pb = find(bb);

        if (pa == pb) return;

        // Union by size
        if (node2size.get(pa) < node2size.get(pb)) {
            int temp = pa;
            pa = pb;
            pb = temp;
        }

        parents.put(pb, pa);
        node2size.put(pa, node2size.get(pa) + node2size.get(pb));
    }
}

class Solution {
    public int removeStones(int[][] stones) {
        int n = stones.length;

        // Group stone indices by row and column
        Map<Integer, List<Integer>> xRows = new HashMap<>();
        Map<Integer, List<Integer>> yCols = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int x = stones[i][0];
            int y = stones[i][1];

            xRows.computeIfAbsent(x, k -> new ArrayList<>()).add(i);
            yCols.computeIfAbsent(y, k -> new ArrayList<>()).add(i);
        }

        DSU dsu = new DSU();

        // Union stones sharing the same row
        for (List<Integer> row : xRows.values()) {
            int first = row.get(0);

            for (int j = 1; j < row.size(); j++) {
                dsu.union(first, row.get(j));
            }
        }

        // Union stones sharing the same column
        for (List<Integer> col : yCols.values()) {
            int first = col.get(0);

            for (int j = 1; j < col.size(); j++) {
                dsu.union(first, col.get(j));
            }
        }

        // Count connected components
        Set<Integer> roots = new HashSet<>();

        for (int i = 0; i < n; i++) {
            roots.add(dsu.find(i));
        }

        return n - roots.size();
    }
}