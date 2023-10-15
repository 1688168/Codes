class Solution {
public:
    int minMovesToMakePalindrome(string s) 
    {
        int n = s.size();
        int ret = 0;
        int count = 0; // how many left-pair characters have been processed
        
        for (int i=0; i<n/2; i++)
        {            
            int j = n-1-count; //starting point to search the right char of the pair
            while (s[j]!=s[i]) j--;
            if (i==j) //the center char case
            {
                int k = n/2-j;
                ret += k;
            }
            else
            {
                int k = n-1-count-j;
                ret += k;
                while (k--)//physically swap the char
                {
                    swap(s[j], s[j+1]);
                    j++;
                }         
                count++;
            }
        }
        
        return ret;
    }
};