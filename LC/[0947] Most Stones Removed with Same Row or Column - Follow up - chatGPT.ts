function removeStonesSequence(stones: number[][]): number[][] {
    /*
     * Each stone is a graph node.
     * Two stones are connected if they share a row or column.
     * For each connected component, keep one root stone and remove all others.
     * Use DFS postorder so children are removed before parents.
     */

    const n = stones.length;

    const rowMap = new Map<number, number[]>();
    const colMap = new Map<number, number[]>();

    // Use each stone's index as its graph node id.
    for (let i = 0; i < n; i++) {
        const [x, y] = stones[i];

        if (!rowMap.has(x)) rowMap.set(x, []);
        if (!colMap.has(y)) colMap.set(y, []);

        rowMap.get(x)!.push(i);
        colMap.get(y)!.push(i);
    }

    // Graph representation as an adjacency list.
    const graph: number[][] = Array.from({ length: n }, () => []);

    function connectGroup(indices: number[]): void {
        if (indices.length <= 1) return;

        const first = indices[0];

        for (let i = 1; i < indices.length; i++) {
            const other = indices[i];

            // Add undirected edge: first <-> other.
            graph[first].push(other);
            graph[other].push(first);
        }
    }

    // Connect stones sharing the same row.
    for (const indices of rowMap.values()) {
        connectGroup(indices);
    }

    // Connect stones sharing the same column.
    for (const indices of colMap.values()) {
        connectGroup(indices);
    }

    const visited = new Array<boolean>(n).fill(false);
    const removalOrder: number[] = [];

    function dfs(node: number, isRoot: boolean): void {
        visited[node] = true;

        // Visit children/neighbors first.
        for (const nei of graph[node]) {
            if (!visited[nei]) {
                dfs(nei, false);
            }
        }

        // Postorder: remove this stone only after DFS children are processed.
        // Do not remove the root stone of this component.
        if (!isRoot) {
            removalOrder.push(node);
        }
    }

    // Run DFS for each connected component.
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, true);
        }
    }

    // Convert stone indices back to coordinates.
    return removalOrder.map((idx) => stones[idx]);
}