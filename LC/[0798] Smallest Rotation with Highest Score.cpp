class Solution {
public:
    int bestRotation(vector<int>& A) {
        
        int N = A.size();
        vector<int> diff(N);//[0, N-1]
        for(int ii=0; ii<N; ++ii){
            if(A[ii] <= ii){
                diff[0] += 1;
                diff[(ii-(A[ii]-1))%N] -= 1;
                diff[(ii+1)%N] += 1;
            }else{
                diff[0] += 0;
                diff[(ii+1)%N] += 1;
                diff[(ii+1+N-A[ii])%N] -= 1;

            }
        }

        int score = 0;
        int maxScore = 0;
        int ret = 0;
        for(int kk=0; kk<N; ++kk){
            score += diff[kk];
            if(score >maxScore){
                maxScore = score;
            ret=kk;
            }
        }
        return ret;
    }
};