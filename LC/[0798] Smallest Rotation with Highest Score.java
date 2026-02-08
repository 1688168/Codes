class Solution {
    public int bestRotation(int[] nums) {
       int N = nums.length;
    
       /*
       * for each k (rotation) -> what's the score?
       * record min_kk with maxScore
       * for each ii, we can use O(1) to determine score range
       * interval sum of score range for all ii can determin total score given a k
       */
       //define diff array events to collect ranges for each ii
       int[] events = new int[N];//each ii have range [0~N-1]
       
       /*
        > `when nums[ii] > ii`
        //ex1
           ii 0 1 2 3 4 5 //index
           vv x x x 5 x x //value
           kk 3 2 1 0 5 4 //num of rotation
           ss 0 0 0 0 0 1 //score

           kk 0 1 2 3 4 5
           ss 0 0 0 0 1 0

        //ex2 - nums[ii] > ii
           ii 0 1 2 3 4 5 //index
           vv x x 4 x x x //value
           kk 2 1 0 5 4 3 //num of rotation
           ss 0 0 0 0 1 1 //score

           kk 0 1 2 3 4 5 //we start to score 1 when rotate to the end
           ss 0 0 0 1 1 0

        > `when nums[ii] < ii`
           ii 0 1 2 3 4 5 //index
           vv x x x x 2 x //value
           kk 4 3 2 1 0 5 //num of rotation
           ss 0 0 1 1 1 1 //score

           kk 0 1 2 3 4 5
           ss 1 1 1 0 0 1
           
       */
       
       for(int ii=0; ii<N; ++ii){
            if(nums[ii] > ii){
                events[0] += 0; //no rotation, 0 since vv>ii 
                events[(ii+1)%N] += 1; //we start to score 1 when rotate to the end
                events[(ii+1 + N-nums[ii])%N] -= 1; //we continue to rotate and score 1 until ii > nums[ii]
            }else{
                events[0] += 1; //nums[ii] < ii -> starting from 1 since vv >= ii
                events[(ii-nums[ii]+1)%N] -= 1;//maintaining 1 until ii>vv
                events[(ii+1)%N]+=1;//we start to be 1 after rotate to the end. (moving ii+1 is the starting of en)
            }
       }

        //find the max score with min kk

        int mkk = -1; //the smallest k s.t. we reach max_score
        int mxScore = -1;
        int score = 0;
        for(int kk=0; kk<N; ++kk){
            score+= events[kk];
            if(score > mxScore){
                mxScore = score;
                mkk=kk;
            }
        }

        return mkk; 
    }
}