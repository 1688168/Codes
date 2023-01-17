
bool isPalindrome(string arr, int ll, int rr){
    while(ll<rr){
        if(arr[ll]!=arr[rr]) return false;
        ++ll;
        --rr;
    }
    return true;
}

bool validPalindrome(string arr)
{
    /*
    left, right pointer
    when reaching first diff-> return left or right skipping
    if not diff -> true
    */


    int ll=0, rr=arr.size()-1;
    while(ll <rr){
        if(arr[ll]!=arr[rr]){//if encounter diff, we can skip once
            //skip left or right either one true is fine
            return isPalindrome(arr, ll+1, rr) || isPalindrome(arr, ll, rr-1);
        }
        ++ll;
        --rr;    
    }
    //if we can get here, means no diff -> palindrome true
    return true;


}