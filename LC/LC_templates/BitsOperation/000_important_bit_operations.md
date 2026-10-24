## Critical Bit Operations for Interviews

Python syntax. Bit positions start at `0` from the right.

| Operation | Expression | Meaning / Example |
|---|---|---|
| AND | `a & b` | `110 & 101 = 100` |
| OR | `a \| b` | `110 \| 101 = 111` |
| XOR | `a ^ b` | `110 ^ 101 = 011` |
| NOT | `~x` | Flip bits; in Python, `~x == -x - 1` |
| Shift left | `x << k` | Multiply by `2**k` |
| Shift right | `x >> k` | Equivalent to `x // (2**k)` |
| Check bit `k` | `(x >> k) & 1` | Return `0` or `1` |
| Set bit `k` | `x \| (1 << k)` | Make bit `k` equal to `1` |
| Clear bit `k` | `x & ~(1 << k)` | Make bit `k` equal to `0` |
| Toggle bit `k` | `x ^ (1 << k)` | Flip only bit `k` |
| Remove rightmost set bit | `x & (x - 1)` | `1100 → 1000` |
| Isolate rightmost set bit | `x & -x` | `1100 → 0100` |
| Check power of two | `x > 0 and (x & (x - 1)) == 0` | Positive integer with exactly one set bit |
| Count set bits | `x.bit_count()` | `13 = 1101` has `3` set bits |
| Keep lowest `k` bits | `x & ((1 << k) - 1)` | Clear all bits above the lowest `k` |

## XOR Identities

| Identity | Meaning |
|---|---|
| `a ^ a == 0` | Duplicate pairs cancel |
| `a ^ 0 == a` | XOR with zero preserves the value |
| `a ^ b == b ^ a` | Order does not matter |
| `(a ^ b) ^ c == a ^ (b ^ c)` | Grouping does not matter |

## Three Patterns to Prioritize

1. **XOR cancellation:** find a unique number when all others appear twice.
2. **`x & (x - 1)`:** remove the rightmost set bit; useful for counting bits and checking powers of two.
3. **`x & -x`:** isolate the rightmost set bit; useful for separating two unique numbers.

For bit-removal loops and fixed-width masks, assume nonnegative integers unless you explicitly handle negative values.