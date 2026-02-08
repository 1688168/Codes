# [0798] Smallest Rotation with Highest Score
## Analysis

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