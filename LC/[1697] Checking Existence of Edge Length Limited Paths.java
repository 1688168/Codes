class DSU{
    private final Map<Integer, Integer> parents;
    private final Map<Integer, Integer> size;

    DSU(int n){
        parents = new HashMap<>();
        size = new HashMap<>();

        for(int ii=0; ii<n; ++ii){
            find(ii);
        }
    }

    public void union(int aa, int bb){
        int pa=find(aa);
        int pb=find(bb);
        if(pa==pb) return;
        if(size.get(pa) < size.get(pb)){
            int tmp = pa;
            pa=pb;
            pb=tmp;
        }

        parents.put(pb, parents.get(pa));
        size.put(pa, size.get(pa) + size.get(pb));

    }

    public int find(int xx){
        if(!parents.containsKey(xx)){
            parents.put(xx, xx);
            size.put(xx, 1);
        }

        if(xx != parents.get(xx)){
            parents.put(xx, find(parents.get(xx)));
        }

        return parents.get(xx);
    }
}

class Solution {
    public boolean[] distanceLimitedPathsExist(int n, int[][] edgeList, int[][] queries) {
        DSU dsu = new DSU(n);

        //sort the edgeList by weight
        Arrays.sort(edgeList, (aa, bb) -> Integer.compare(aa[2], bb[2]));

        //sort the query order
        Integer[] queryOrder = new Integer[queries.length];
        for(int ii=0; ii< queries.length; ++ii){
            queryOrder[ii] = ii;
        }

        Arrays.sort(queryOrder, (aa, bb)-> Integer.compare(queries[aa][2], queries[bb][2]));

        //now we query one by one
        int edgeIdx = 0;
        boolean[] ans = new boolean[queries.length];

        for(var orderId: queryOrder){
            int aa = queries[orderId][0];
            int bb = queries[orderId][1];
            int ll = queries[orderId][2];

            for(int ii=edgeIdx; ii<edgeList.length; ++ii){
                int an=edgeList[ii][0];
                int bn=edgeList[ii][1];
                int ww=edgeList[ii][2];
                if(ww < ll){
                    dsu.union(an, bn);
                    ++edgeIdx;
                }else{
                    break;
                }
            }

            ans[orderId] = dsu.find(aa) == dsu.find(bb);
        }

        return ans;
    }
}

/*
# if we do DFS on every node: we will have
* DFS: O(V+E) - 10^5
* N queries: -> 10^5*10^5 -> TLE

* each query is asking if two nodes are connected with all edge length < limit
* if we only have 1 query and not using DFS (we are unable to scale per above)
* whether two nodes are connected -> DSU
* whether two nodes are connected with all edges less than limit -> build the DSU with edges less than limit and ask if the two nodes are connected


*/
 
