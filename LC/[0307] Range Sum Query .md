# <span style="color:Green">Binary Index Tree </span>

- subset of Segment Tree
- why we still need Binary Index Tree if Segment Tree can solve? -> much less coding
- used to calc range sum with update
- http://www.cnblogs.com/grandyang/p/4985506.html
- Use less than O(N) time to find subarray sum

### The template is 1 indexed

- Template: https://github.com/wisdompeak/LeetCode/blob/master/Template/Binary_Index_Tree/BIT.cpp

- Python solution: https://yunrui-li.medium.com/leetcode-binary-index-tree-59fc04d8d20d

# <span style="color:Green">Segment Tree </span>

```
                         [0,9]
                [0,4]                                      [5,9]
    [0,2]                  [3,4]                      [5,7]         [8,9]

[0,1]      [2, 2]        [3, 3] [4,4]            [5,6]     [7,7]   [8,8][9,9]
[0,0] [1,1]                                [5,5][6,6]

```

- <span style="color:red">single point update: log(N)</span>
- <span style="color:red">range query: log(N) </span>
