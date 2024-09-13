* choose 15 out of 30
* N=15 -> implying bruteforce
* Take first N out of the 2N
* First Half 2^15 => i, x where i indicate num of elements chosen in first N, x=sum1
* Second Half: N-ii, y (need to be selected)

x+y ~= sum-(x+y) //sum of selected (from both first/second) should be close to sum of those that is not selected
=> 2(x+y) ~= sum
=> y ~= sum/2 - x

map[j]={y1, y2, ..., yj} //given num need from 2nd half, what are the potential sum2?

=> given i, x -> binary search from map s.t. y~= sum/2-x
=> ret = min(ret, abs(sum-2(x+y)))

> complexity analysis  
>> 2nd half
* O(2^n*n)
-> for each j: 2^n (total number of J ~ 30k)
-> calc sum: n

>> 1st half:traverse and binary serch 2nd half
* O(2^n * log(2^n)) = o(2^n*n)
> why 双向奔赴？
