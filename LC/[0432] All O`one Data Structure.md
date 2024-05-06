> Requirements
* kv inc/desc O(1)
* return (any key) min/max with O(1) cost

> Analysis
![432](../rcs/432.png)
+ There is no Double Linked List in Python Standard Library.  If you need to use (double) Linked List -> use C++ for the solution
+ C++ list is double linked list
+ for O(1) random access
    - we will need double linked list to maintain order
    - we will need a key2iter map to determin which node in the list for operation

+ KV O(1) operation: k2v dictionary
+ min/max -> freq sorted front for min, back for max