## Word Ladder
[Word Ladder I](https://leetcode.com/problems/word-ladder/submissions/ "BFS" )
Given 1. Begin word (might not be in the dictionary)
      2. dictionary
      3. end word (part of dictionary)
Objs: Shortest transformation sequence to move from begin word to end word
      and each step change one letter that is in the dictionary
Solution Plan：
1. Build graph define connected words.  See below how to calc connected words.
2. BFS until we reach ending words
3. output a path

Q: how do we identify all connected words?
 a. O(N^2):
    Try each pair
 b. O(N*L*25):
    Given a word (all lowercase English letters), replace with a diff letter and
    see if the new word in the dictionary

 Evaluation per constraint:
 * wordList size: max=5,000
               -> N^2
               -> 25,000,000  <<<<<
 * word_length:  max=10
               -> 10*25
               -> 250         <<<<< this is way faster

=> so we choose option B

[Word Ladder II](https://leetcode.com/problems/word-ladder-ii/ "BFS")
Same as word ladder I, but need to print all the feasible paths as output

Solution Plan:
- Apply solution in I.
- while building the BFS, we also record the parents (reversed graph)
- do a DFS to output all paths
