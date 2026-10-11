class DSU{
    private Map<Integer, Integer> parent;
    private Map<Integer, Integer> node2size;

    DSU(){
        this.parent = new HashMap<>();
        this.node2size = new HashMap<>();
    }

    public void union(int aa, int bb){
        var pa = find(aa);
        var pb = find(bb);
        if(pa==pb) return;

        if(this.node2size.get(pa) < this.node2size.get(pb)){
            var tmp = pa; 
            pa=pb;
            pb=tmp;
        }

        this.parent.put(pb, pa);
        this.node2size.put(pa, this.node2size.get(pa) + this.node2size.get(pb));
    }

    public int find(int xx){
        if(!this.parent.containsKey(xx)){
            this.parent.put(xx, xx);
            this.node2size.put(xx, 1);
        }


        if(this.parent.get(xx) != xx){
            this.parent.put(xx, this.find(this.parent.get(xx)));
        }

        return this.parent.get(xx);
    }

}

class Solution {
    public int removeStones(int[][] stones) {
        int N = stones.length;
        //build DSU: we need to union all pairs
        //build the connected graph first so we know all the neighbors
        Map<Integer, List<Integer>> xRows = new HashMap<>();
        Map<Integer, List<Integer>> yCols = new HashMap<>();
        for(int ii=0; ii<N; ++ii){//O(N)
            int xx = stones[ii][0];
            int yy = stones[ii][1];
            xRows.computeIfAbsent(xx, kk -> new ArrayList<>()).add(ii);
            yCols.computeIfAbsent(yy, kk -> new ArrayList<>()).add(ii);
        }

        Map<Integer, List<Integer>> gg = new HashMap<>();
        for(var x_row: xRows.values()){
            var first = x_row.get(0);
            for(int jj=1; jj<x_row.size(); ++jj){
                var other = x_row.get(jj);
                gg.computeIfAbsent(first, kk -> new ArrayList<>()).add(other);
                gg.computeIfAbsent(other, kk-> new ArrayList<>()).add(first);

            }
        }

        for(var y_col: yCols.values()){
            var first = y_col.get(0);
            for(int jj=1; jj<y_col.size(); ++jj){
                var other = y_col.get(jj);
                gg.computeIfAbsent(first, kk -> new ArrayList<>()).add(other);
                gg.computeIfAbsent(other, kk-> new ArrayList<>()).add(first);
            }
        }

        //build DSU
        var dsu = new DSU();
        //union all pairs
        for(var entity: gg.entrySet()){
            var key = entity.getKey();
            var values = entity.getValue();
            for(var yy: values){
                dsu.union(key, yy);
            }
        }

        //return N-totalNumOfGroups

        Set<Integer> roots = new HashSet<>();
        for(int ii=0; ii<N; ++ii){
            roots.add(dsu.find(ii));
        }
        return N -  roots.size();
    }
}



// // Union all connected pairs
// for (Map.Entry<Integer, List<Integer>> entry : gg.entrySet()) {
//     int node = entry.getKey();
//     List<Integer> neighbors = entry.getValue();

//     for (int neighbor : neighbors) {
//         dsu.union(node, neighbor);
//     }
// }