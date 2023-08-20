using LL = long long;
LL M = 1e9+7;
class Solution {
public:
    int sumOfPower(vector<int>& nums) 
    {
        sort(nums.begin(), nums.end());
        
        LL sum = 0;
        LL ret = 0;
        
        for (int i=0; i<nums.size(); i++)
        {
            LL mx = (LL)nums[i]*(LL)nums[i]%M;
            
            if (i>=1)
                sum = sum * 2 % M + (LL)nums[i-1];
            
            ret += mx * sum % M + mx * nums[i] % M;
            ret %= M;
        }
        
        return ret;
    }
};


/* my stupid solution*/
using LL = long long;
LL M = 1e9 + 7;

class Solution {
public:
    int sumOfPower(vector<int>& nums) {
       
        sort(nums.begin(), nums.end()); //nlog(n)
        /*
        ex:  
            x y z a b //sorted array
            ^         //let x be the max of a group,  
                      //min can only be x

            min power
            x   x^2 * x  //self + no other options 
                     ^^^^^^^^ let this as A
        => self^2* (self+0*2)

        --------------------------------------------------
            x y z a b //sorted array
              ^       //let y be the max of a group,  
                      //min can be x or self

            min power
            y   y^2 * y  //self
            x   y^2 * x 
        => self^2*(x+y) => self^2 * (x+y)
                        => self^2 * (self+x+prev*2)
        ---------------------------------------------------
            prev=0
            prev=x

            x y z a b //sorted array
                ^     //let z be the max of a group,  
                      //min can be x, y

            min power
            z   z^2 * z  //self
            y   z^2 * y 
            x   z^2 * x * 2 //everything in between has two options -> 2^(ii-2) options
            => self^2 (self + y + prev*2 )

        ---------------------------------------------------    
        */
        LL ans = 0;
        LL N = nums.size();
        LL acc = 0;
        for(int ii=0; ii<N; ++ii){//for each ii as the max 
            LL mx = (LL)nums[ii]*(LL)nums[ii]%M;

            if(ii >= 1){
                ans = (ans%M + mx*nums[ii]%M + (mx*nums[ii-1])%M + ((mx*acc)%M*2)%M)%M;
                //ans = (ans%M + (mx*(((nums[ii]+ nums[ii-1])%M + (acc*2)%M)%M)%M)%M)%M;
                acc = ((acc*2)%M + nums[ii-1])%M;
            }else{
                ans = (mx*nums[ii])%M; //min, max is itself
                acc = 0;
            }

        }

        return ans;
    }
};