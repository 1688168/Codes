[`Notes`]
* when you deal with palindrome, start from what is palindrome: s equal to s' (it's reversal)
* when we are given a single string and asking to make it a palindrome by some editing, this is equivalent of asking given s and s' (where s' is reversal of s).  and asking the required operations to make s and s' the same.
* we know given s and t, two strings, the min operations to make s and t the same (relating to LCS, SCS)
* the question now is given s and s', the min operations to make s and s' the same.  in such case, LCS and SCS are both palindrome. (cuz s' is the reversal of s)

[`Interval DP`]
* from small interval to bigger interval (the base case)
* if smaller interval is palindrome, increase interval size and try build new state on top of the old state

[`Shortest-common-super-sequence`]
* the Shortest-Common-Subsequence (SCS) of S and SS (where SS is the reverse of s) is a palindrome
* min add to make two strings the same -> len(scs)-len(s)
* if the two string is s it's reversal (ss) -> SCS makes s and ss the same. -> s and it's reversal the same -> SCS is a palindrome