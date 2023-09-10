from collections import defaultdict, deque


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        """
        1. g2members: ungrouped members are assigned with unique new groupID
        2. gm, idtm: for topology sort within group
        3. gg, idtg: for topology sort groups
        4. g2sortedMembers
        """

        res = []
        nextGID = m
        # ----- Build relationship groups
        # Build graph and indgree table for nodes in same groups
        gm = defaultdict(set)  # graph for same group nodes
        gg = defaultdict(set)  # graph for inter group nodes
        idtm = {}
        idtg = {}
        g2members = defaultdict(set)

        for ii in range(n):  # for each node
            if group[ii] == -1:
                group[ii] = nextGID
                nextGID += 1
            g2members[group[ii]].add(ii)

        for ii in range(n):
            for jj in beforeItems[ii]:
                if group[ii] != group[jj]:  # nodes ii, jj in diff group
                    gi = group[ii]
                    gj = group[jj]
                    if gj not in gg:
                        gg[gj].add(gi)
                        idtg[gi] = idtg.get(gi, 0) + 1
                    else:
                        if gi not in gg[gj]:
                            gg[gj].add(gi)
                            idtg[gi] = idtg.get(gi, 0) + 1
                else:  # node ii, jj in same group
                    if jj not in gm:
                        gm[jj].add(ii)
                        idtm[ii] = idtm.get(ii, 0) + 1
                    else:
                        if ii not in gm[jj]:
                            gm[jj].add(ii)
                            idtm[ii] = idtm.get(ii, 0) + 1

        # ----- Define topology sort helper
        def topology_sort(nodes, g, idt):
            dq = deque()
            res = []

            for n in nodes:
                if n not in idt:
                    dq.append(n)

            while len(dq) > 0:
                curr = dq.pop()
                res.append(curr)

                for c in g[curr]:
                    idt[c] -= 1
                    if idt[c] == 0:
                        dq.append(c)

            if len(res) != len(nodes):
                return None

            return res

        # ----- sort within group
        # output dict g2sortedMembers
        g2sortedMembers = defaultdict(list)
        for gid, gmembers in g2members.items():  # sort each group
            # print(" sort gid: ", gid, " members: ", gmembers)
            sorted_members = topology_sort(gmembers, gm, idtm)
            if sorted_members is None:
                return list()
            # print(" sorted members: ", sorted_members)
            g2sortedMembers[gid] = sorted_members

        # ----- sort intra groups
        # output list of sorted groupID
        groups = {gid for gid in g2members}
        sorted_groups = topology_sort(groups, gg, idtg)
        if sorted_groups is None:
            return list()

        # ----- output order
        for g in sorted_groups:
            for m in g2sortedMembers[g]:
                res.append(m)

        return res
