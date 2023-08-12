# Array:
** put all same element in the array together **
- if all elements are from 26 lowercase letters
-> declare [[]*26]
-> traverse the string append location of each char into array under ord of that chars
-> now we know each element's prev/next location

** Element contribution to subarray in order to calc an aggregated result **
- Given an array, definition of an attribute for a subarrays, and calc max, min, aggregation of all subarrays on this attribute.
- sum of unique char cnt for all subarrays (how do you find unique char's prev/next?)
- define variance of subarray (max-min char cnt in each subarray) -> calc sum of all subarray variance.
- define power of subarray


** Range: (max-min) in subarrays -> return sum of all subarray ranges
