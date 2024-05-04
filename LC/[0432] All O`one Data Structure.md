> Requirements
* kv inc/desc O(1)
* return (any key) min/max with O(1) cost

> Analysis
+ KV O(1) operation: k2v dictionary
+ min/max -> freq sorted front for min, back for max