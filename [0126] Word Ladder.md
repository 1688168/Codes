## Word Ladder  
[Word Ladder I](https://leetcode.com/problems/word-ladder/submissions/ "BFS" )  
Given 1. Begin word (might not be in the dictionary)  
      2. dictionary  
      3. end word (part of dictionary)  
Objs: Shortest transformation sequence to move from begin word to end word
      and each step change one letter that is in the dictionary

Q: how do we identify all connected words?  
 a. try each pair: O(N^2)  
 b. given a word (all lowercase English letters), replace with a diff letter and
    see if the new word in the dictionary
    O(N*L*25)
 => constraint: wordList size 1~5,000 => N^2   => 25,000,000  
                word_length: 1~10     => 10*25 => 250  

=> so we choose option B  

[Word Ladder II](https://leetcode.com/problems/word-ladder-ii/ "BFS")  
Same as word ladder I, but need to print all the feasible paths as output  
