# Problem Statement
## Given
* n: num of digits of the password
* k: each digit of the password could be in the range [0, k-1]

## ask
* shortest string that contains all potential possibles that can be constructed given (n, k)

# Constraints analysis
* 1 <= n <= 4 → each password has exactly n digits, at most 4.
* 1 <= k <= 10 → each digit can be from 0 to k - 1.
* Given n and k, there are k^n possible passwords, and we can generate all of them.
* 1 <= k^n <= 4096 → there are at most 4096 possible passwords, so tracking each one is manageable.
* Trying every ordering of these passwords and merging overlapping digits would be too expensive in the worst case. We need a more efficient way to construct the shortest string covering every password.

# what can we do with edge cases given the constraints -> partial credit
* when n=1 -> return string concatenating 0...k-1
* when k=1 -> return n zeros concatenated

# Algorithm analysis

# Complexity analysis