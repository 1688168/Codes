class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M=len(matrix)
        N=len(matrix[0])

        ll, rr = 0, N-1
        while ll < rr:
            # we need to rotate 3 times for each layer
            for ii in range(rr-ll):
                top, btm = ll, rr
                # save the top-left value
                top_left=matrix[top][ll+ii]

                # copy btm-left to top-left
                matrix[top][ll+ii]=matrix[btm-ii][ll]


                # copy btm-right to btm-left
                matrix[btm-ii][ll]=matrix[btm][rr-ii]


                # copy top-right to btm-right
                matrix[btm][rr-ii]=matrix[top+ii][rr]

                #copy top-left to top-right
                matrix[top+ii][rr]=top_left

            ll+=1
            rr-=1
