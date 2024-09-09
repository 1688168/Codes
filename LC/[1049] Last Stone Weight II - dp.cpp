
/*
>> problem statement: merging any two stones until only one survive or all disappeared
* which means: given list: [a, b, c, ..., zz]
-> assign each element as + or -
-> find the min sum that is >= zero.
* notice each element is either + or -
-> which means: partition the list to group_A and group_B.   A and B are complements.
-> sum(list)=Total=sum(A)+sum(B)
>> revised problem statement: 
-> given a list of num
-> select a subset A from the list s.t. max(sum(A)) <= Total//2 (anything not in A is in B)
-> This falls into a classic knapsack problem.
-> capacity: Total//2
-> profit=nums[ii]
-> cost=nums[ii]
-> what is the max profit?
-> return Total - sum(A)*2 
          Total = sum(B)+sum(A) 
                = (sum(A)+sum(B)-sum(A)) + sum(A))
         Total - sum(A)*2 = sum(B)-sum(A)
         
*/

class Solution {
/*
>> problem statement: merging any two stones until only one survive or all disappeared
* which means: given list: [a, b, c, ..., zz]
-> assign each element as + or -
-> find the min sum that is >= zero.
* notice each element is either + or -
-> which means: partition the list to group_A and group_B.   A and B are complements.
-> sum(list)=Total=sum(A)+sum(B)
>> revised problem statement: 
-> given a list of num
-> select a subset A from the list s.t. max(sum(A)) <= Total//2 (anything not in A is in B)
-> This falls into a classic knapsack problem.
-> capacity: Total//2
-> profit=nums[ii]
-> cost=nums[ii]
-> what is the max profit?
-> return Total - sum(A)*2 
          Total = sum(B)+sum(A) 
                = (sum(A)+sum(B)-sum(A)) + sum(A))
         Total - sum(A)*2 = sum(B)-sum(A)
         
*/
public:
    int lastStoneWeightII(vector<int>& stones) {
        unordered_set<int> Set({0}); //initialize as 0
        
        /*
        * build all potential combination of the +/- sequence
        * find the combination that is the smallest and greater than zero
        */
        for(auto x: stones){//for each stone
            auto Set_temp = Set;
            Set.clear(); //clear the set to accept new subsets
            for(auto s: Set_temp){
                Set.insert(s+x);//only need to record aggregated value
                Set.insert(s-x);
            }   
        }
        
        int result = INT_MAX;
        for(auto x: Set){//for each set
            if(x>=0 & result>x) result=x;//filter out sum >=0 and the smallest
        }
        return result;
    }
};