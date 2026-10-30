class Solution {
    public void rotate(int[][] matrix) {
        int N = matrix.length;
        int ll=0, rr=N-1;
        while(ll<=rr){//for each layer
            int tt=ll, bb=rr;
            for(int ii=0; ii<rr-ll; ++ii){//each layer, we process each cell
                int top_left_tmp = matrix[tt][ll+ii];
                //moving left column to top row
                matrix[tt][ll+ii]=matrix[bb-ii][ll];

                //moving bottom row to left-col
                matrix[bb-ii][ll]=matrix[bb][rr-ii];

                //moving right-col to bottom-row
                matrix[bb][rr-ii]=matrix[tt+ii][rr];

                //moving top-row to right-col;
                matrix[tt+ii][rr] = top_left_tmp;
            }
            ++ll;
            --rr;
        }
    }
}