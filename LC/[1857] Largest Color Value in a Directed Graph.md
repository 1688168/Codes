## Problem statements:

- The <span style="color:red">**Color Value**</span> of the path is the number of nodes that are colored the most frequently occurring color along that path => <span style="color:red">_**the color in the path with highest frequency**_</span>
- return largest "_Color Value_"

## Analysis:

- we cannot possible try all paths and calc the highest freq color
- we only care about from leaf-node to leaf-node
- We also need to detect cycle (Topology sort)
- We have at most 26 colors
- for each color (26 times at most), count it's highest frequency per BFS from leaf ending on leaf
