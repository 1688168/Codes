class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        """
        ---------------- log timeseries
        query if sorted by time, we only need to scan the log timeseries one time
        moving the query as a window:  (q[i]-x, q[i]) and maintain a dict recording what servers in the window
        n-size(dict) is the cnt of server that is NOT in the window
        
        """
        res=[0]*len(queries)          # ready to host this number of queries
        logs.sort(key=lambda x: x[1]) # sort logs by time
        qries=[(ii, tt) for ii, tt in enumerate(queries)] # sort queries by time
        qries.sort(key=lambda x:x[1])

        # define the window
        ll, rr = 0, 0
        server2cnt={}
        for server_id, ts in qries: # check each query
            # move the right border
            while rr < len(logs) and logs[rr][1] <= ts:
                server2cnt[logs[rr][0]] = server2cnt.get(logs[rr][0], 0)+1
                rr+=1
            
            while ll < len(logs) and logs[ll][1] < ts-x:
                server2cnt[logs[ll][0]] -= 1
                if server2cnt[logs[ll][0]] == 0: del server2cnt[logs[ll][0]]
                ll+=1
            
            res[server_id]=n-len(server2cnt)

        return res