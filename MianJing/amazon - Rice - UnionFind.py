"""
You are shopping on Amazon.com for some bags of rice.
Each listing displays the number of grains of rice that the bag contains.
You want to buy a perfect set of rice bags from the entire search result list, riceBags.
A perfect set of rice bags, perfect, is defined as:

The set contains at least two bags of rice
When the rice bags in the set perfect are sorted in increasing order by grain count,
it satisfies the condition perfect[i] * perfect[i] = perfect[i + 1] for all 1 ≤ i < n.
Here n is the size of the set and perfect[i] is the number of rice grains in bags i.
Find the largest possible set perfect and return an integer, the size of that set.
If no such set is possible, then return -1. It is guaranteed that all elements in riceBags are distinct.
"""
