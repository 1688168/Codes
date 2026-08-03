# LC 127 - Word Ladder
## Problem Statement
> Given 
* Begin Word (BGW)
* End Word (EDW)
* a word list
* transformation sequence BGW->s1->s2...->EDW

> Ask
* numOfWords in the shortest transformation sequence

> Notice
* BGW might not be in the worklist

> In Short:
* transforming BGW (each time one char) in word sequence (s1, s2, edw). s1, s2, ..., sk need to be in work list
* num of shortest path
* N= 5k -> N^2
* word_len=10
  
## Thoughts
* shortest distance -> BFS -> we need to build the tree/graph to represent the givne data
* BFS needs queue
* hit -
      -
      -
* if we list all valid next word and avoid circling, we can rely on BFS find the shortest path

> how do you find the valid next candidate
> how do you avoid circling?

* loop the word char by char: 10
* for each char, we try replace all 26 char and look up if existing in word list (prebuild set)
  * check if we are final word if so short circuit and return

## Refined Thought process
1. the question is asking for the shortest distance -> BFS
    * know the BFS template (dequeue)
  
2. in order to do BFS, we need to first convert the given data to a graph or a tree.  since each word could have many or uncertain neighboring words -> graph is a better data model
3. Complexity analysis
> build tree
* for each word (5000), we need to try each char (10) with all potential replacing char (26) -> 5000*10*26=1.3MM
* BFS -> 


## To practice
1. Time complexity analysis for BFS
2. Hows to build a graph, the required data structure
3. How to do BFS
4. How to do this without build graph first