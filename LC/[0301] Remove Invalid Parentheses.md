1. First determine the final length by calc how many parenthesis need to be removed (LC921)
2. Find all valid possible results

ex: we need to eliminate 2
(((( ))

valid= C(4, 2) = 6 # dfs will produce 6 outcomes, but they are all the same
ans=(())

How to eliminate duplicates?

xxoo
xoxo
xoox
oxox
ooxx
xoox

- naive DFS, we will try above 6 but the end result is the same "(("
- so we apply the following strategy on DFS that will significantly reduce the search space

ex: we need to select two A

B A _ A _ A_A
^
curr
b x x x X => B #empty after B
b x x x A => BA
b x x A A => BAA << only one result per this strategy (instead of 6 above)
b x A A A => BAAA
b A A A A => BAAAA

by the strategy below, we avoids try all pow(2, 4) potential selection

### the strategy for pruning repeats

1. if s[i] != res[-1]
   option1(select): res+s[ii] ...
   option2(skip): res ...

2. if s[i] == res[-1]:
   option1(must select): res + s[ii]

**conclusion:**
if we need to select multiple A, the strategy above will help us get the last multiple A
