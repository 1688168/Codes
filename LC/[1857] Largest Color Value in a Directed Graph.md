## Problem statements:

- The <span style="color:red">**Color Value**</span> of the path is the number of nodes that are colored the most frequently occurring color along that path => <span style="color:red">_**the color in the path with highest frequency**_</span>
- return largest "_Color Value_"

## Analysis:

- we cannot possible try all paths and calc the highest freq color
- we only care about from leaf-node to leaf-node
- We also need to detect cycle (Topology sort)
- We have at most 26 colors
- for each color (26 times at most), count it's highest frequency per BFS from leaf ending on leaf


## V2:
1. build graph and idt
2. BFS the nodes from each leaf node
3. maintain a color2max_freq to record the max_freq 
4. before entering the while loop, initialize the leaf-node color freq table
5. before adding each child, we need to update the child node color freq ( cannot rely on prev node. if we rely on prev node, we might lose info for earlier levels that has higher freq on the color)