"""
username
website
timestamp
1. construct all combinations of 3 websites
2.
"""
from collections import defaultdict
from pprint import pprint as pp
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        # array size = N (max=50)
        # all 3 combination: 50^3= 2500*50=125,000
        # given a user (50): list of visited websites sorted by time
        # calc 3 combinations
        # map[a_combination]=count
        # running max_score
        """

        user2visits=defaultdict(list)
        pattern2score=defaultdict(set)
        max_pattern=""
        max_score=0

        # build user2visits

        for ii in range(len(username)):
            (uu, ww, tt)=username[ii], website[ii], timestamp[ii]

            user2visits[uu].append([tt, ww])

        #pp(user2visits)
        # calc pattern score
        for uu, visits in user2visits.items():
            visits.sort()
            n=len(visits)
            for ii in range(n):
                for jj in range(ii+1, n):
                    for kk in range(jj+1, n):
                        pattern=visits[ii][1]+":"+visits[jj][1]+":"+visits[kk][1]
                        #print("uu: ", uu, " pattern: ", pattern, " ii: ", ii, " jj: ", jj, " kk: ", kk)
                        pattern2score[pattern].add(uu)
                        if len(pattern2score[pattern]) > max_score:
                            max_score=len(pattern2score[pattern])
                            max_pattern=pattern
                        elif len(pattern2score[pattern])== max_score:
                            if pattern < max_pattern:
                                max_pattern=pattern

        #pp(pattern2score)
        ans=max_pattern.split(":")

        return ans

        
