> The Greedy strategy

- for each left char, find the right hand pair and move
- Why is this a valid strategy?
  Consider
  x x y y
  x y x y

x---a---x---b---y---c---y---d
I. move x first:
x2: b+1+c+1+d
y1: b+a
y2: d
=> b + 2 + c + d + b + a + d
=> a+2b+c+2d+2 -------- A

II. move y first
y1: b+2+a
y2: d
x1: 0
x2: b+c+d

=> a+b+2+d+b+c+d
=> a+2b+c+2d+2 ------- B

A==B => it doesn't matter which one you move the result is the same

Try x y x y -> this will also confirm the strategy.

Execution plan:

1. for each left char, find the right pair and physically move
2. if we encounter odd char, just leave it to the last but calc the required move

> The Reverse Pair strategy (cf. 493)

1. Move all paired chars the first half to the left of the string
2. the center char move calc:
   i + (n//2-count) - N//2
   - Counte is the processed pair upto i (the current char which is a center char)
   - i is the current index (the center char)
   - n//2-count: since we definitly has solution, the renmaining pair count is n//2-count
   - so the ii (the center char) eventually will be shifted to i + (n//2-count)
   - moving it back to center costs i+(n//2-count)-N//2 => ii-count
3. re-arrange (per reverse pairs) right substring per left hand side order

0123456789
abyyxccaxb
36789
abyxc|ycaxb
cxyba
68397 => 3 (the reverse pairs calc)

cf 493: reverse pair
The minimum adjacent swaps to make it sorted = # of reverse pairs
