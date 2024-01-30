这是一道真正的Hard。

Objective: find the subsequence with largest kth sum

Step I: (Convert the problem to finding finding top K smallest abs(nums[ii]))

a. Let A be the sum of all postive elements -> A is the max sum of all subsequence from nums
b. the next max sum is A -abs(nums[ii])
   i.e. A + a negative num from nums
    or A - a postive num from exiting selected subsequence
c. follow ideas described in b, we can find kth largest sum
d. => the kth sum is A - (top k smallest abs(nums[ii]))

Step II: build all subsequence sum from a postive array
a. special handling empty set
b. sort nums
c. push (sum, ii)=(nums[0],0) to a min_heap, where sum is a aggregation of list ending @ nums[ii]
d. each time we pop an element from min_heap, we push back the following two operations
    d1: push(sum-nums[ii]+nums[ii+1], ii+1) -- Op1
    d2: push(sum+nums[ii+1], ii+1)          -- Op2
e. the (k-1) element popped from min_heap is the kth subsequence sum from the positive list


Step III: proof step II
I: the algorithm defined in II covers all subsequences
II: this algorithm will not produce duplicate subsequences
III: prove that the sum of subsequences constructed by above algorithm is increasingly sorted.

第三步：证明这个构造方法的正确性
首先，我们要证明这个构造方法覆盖了所有的子序列。这个直观上不难理解。我们考虑，如果已经生成了所有以nums[0]，nums[1]，... nums[i-1]结尾的子序列，那么能否通过之前定义的方法，生成所有以nums[i]结尾的子序列呢？假设某个以nums[i]结尾的子序列，它的倒数第二个元素是任意的nums[k]，那么我们必然可以通过一个以nums[k]结尾的子序列做一次操作2，再反复进行操作1，就可以得到。

其次，我们要证明这个构造方法不会产生重复的子序列。这个也显然，对于任意形如{X,X,...,X,nums[k],nums[i]}的序列，如果k+1==i，那么它必然唯一由形如{X,X,...,X,nums[k]}的子序列通过一次操作2得到；如果k+1!=i，那么它必然唯一由形如{X,X,...,X,nums[k],nums[i-1]}的子序列通过一次操作1得到。

最后，我们要证明这个构造方法生成的子序列是按照和递增的。这个证明很简洁。假设某个序列A小于序列B，但是B先从队列里弹出，这可能吗？注意，这意味着B在队列里的时候A一定还没有加入队列里（否则PQ会优先弹出A）。既然A不在队列里，说明A的前驱状态A'（上一段证明了存在唯一的A'）也必然不会在队列里，因为A'是小于A的，A'在队列的话更会比B优先弹出，从而导致将A也被导入队列里。同理证明，A'的前驱序列A''也不会在队列里，A''的前驱序列也不会在队列里... 但是所有的序列都是从{nums[0]}开始的，难道这个序列也从未加入过队列吗？从而引发矛盾。

综上，我们证明了这种构造方法一定会一个不漏、一个也不重复地、按从小到大的顺序弹出所有的子序列之和。显然第k-1个弹出来的就是第k小的子序列之和（考虑空集）。