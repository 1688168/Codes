1. First determine the final length by calc how many parenthesis need to be removed (LC921)
2. Find all valid possible results

ex: we need to eliminate 2
(((( ))

valid= C(4, 2) = 6 # dfs will produce 6 outcomes, but they are all the same
ans=(())

How to eliminate duplicates?