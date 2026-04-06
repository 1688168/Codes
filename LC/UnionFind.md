# Union Find

## Use Case
* given a set of relationships/connections, how many groups?


## Data Model
* define ancestor as array or dictionary


## strategy
* initialize ancestor as self
* need to process each node and union those nodes that is connected, ignore all others
* union: connected node should have same ancestor (no need to find the ultimate ancestor, just make ancestor the same)
* find: find the ultimiate ancestor
  