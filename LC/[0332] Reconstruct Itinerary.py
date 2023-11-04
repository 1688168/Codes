class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        - need to have the itinerary that has the smallest lexical order 
        - we are leveraging B + path2 + path1, so we need to start from larger 
          lexical words so leaving smaller lexical words to path2
        1. sort (in reversed order)
        2. build graph
        3. dfs from "JFK"
        4. while loop on g["start"]
        5. we will get back path1 (ending @ end) first and path2 in 2nd loop (ending @ B)
        6. paths=[path1, path2] 
        7. remember path1, path2 elements as of now are in reversed lexical order
        8. output path2, path1 to result and return result as one path  
        """
        # sort the string in reversed lexical order (B+path2+path1) strategy
        tickets.sort(reverse=True)

        # we cannot use set since we need to maintain order
        g = collections.defaultdict(list)
        for a, b in tickets:  # build the graph
            g[a].append(b)  # this is appended in reversed order.

        def dfs(start):
            result = [start]
            paths = []

            # this will dfs all child in  lexical order (since we pop from the end of list)
            while len(g[start]) > 0:  # we will get path1 first, and get path2 (if lucky, path1 only)
                # to avoid repeat visiting same edge, remove the edge after visiting
                # we are getting the smallest lexical node from the end, here it shows why we sort in reversed order
                nxt = g[start].pop()
                # we will only get two paths, since this is guaranteed as Eulerian Path
                paths.append(dfs(nxt))

            # paths=[path1, path2]
            # after reverse, we are in lexical order
            # paths=[path1, path2], so we need to output path2 first (reversed)
            for p in reversed(paths):
                for n in p:
                    result.append(n)

            return result

        # dfs
        return dfs("JFK")  # start from "JFK" per requirement
