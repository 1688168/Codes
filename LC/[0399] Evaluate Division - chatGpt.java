class Solution {
    private static class Edge {
        String variable;
        double weight;

        Edge(String variable, double weight) {
            this.variable = variable;
            this.weight = weight;
        }
    }

    private final Map<String, List<Edge>> graph = new HashMap<>();

    public double[] calcEquation(
        List<List<String>> equations,
        double[] values,
        List<List<String>> queries
    ) {
        graph.clear();

        // Build the bidirectional weighted graph.
        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0);
            String b = equations.get(i).get(1);

            // a / b = values[i]
            graph.computeIfAbsent(a, key -> new ArrayList<>())
                 .add(new Edge(b, values[i]));

            // b / a = 1 / values[i]
            graph.computeIfAbsent(b, key -> new ArrayList<>())
                 .add(new Edge(a, 1.0 / values[i]));
        }

        double[] results = new double[queries.size()];

        for (int i = 0; i < queries.size(); i++) {
            String source = queries.get(i).get(0);
            String target = queries.get(i).get(1);

            if (!graph.containsKey(source) ||
                !graph.containsKey(target)) {
                results[i] = -1.0;
                continue;
            }

            Set<String> visited = new HashSet<>();
            visited.add(source);

            results[i] = dfs(source, target, visited);
        }

        return results;
    }

    private double dfs(
        String current,
        String target,
        Set<String> visited
    ) {
        if (current.equals(target)) {
            return 1.0;
        }

        for (Edge edge : graph.get(current)) {
            String next = edge.variable;

            if (visited.contains(next)) {
                continue;
            }

            visited.add(next);

            double remainingValue = dfs(next, target, visited);

            if (remainingValue != -1.0) {
                return edge.weight * remainingValue;
            }
        }

        return -1.0;
    }
}