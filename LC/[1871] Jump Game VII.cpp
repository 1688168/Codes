class Solution { //O(N) solution
public:
    bool canReach(string s, int minJump, int maxJump) {

        if (s.back()=='1') return false;
        int N=s.size();

        vector<int> diff(N+1);

        //marking for idx=0
        diff[0+minJump]=1;
        diff[0+maxJump+1]=-1;
        int reach=0;
        for(int ii=1; ii<N; ++ii){
            reach += diff[ii];
            if(reach==0) continue;
            if(s[ii]=='1') continue;
            if(ii+minJump<=N)diff[ii+minJump] += 1;
            if(ii+maxJump+1<=N)diff[ii+maxJump+1] -= 1; 
        }

        return reach;
    }
};