#####
# 20221018
#####
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        * We want to calc score of pattern and return the pattern with highest score
        *
        """
        # 0. need to sort per visit time for pattern
        # 1. find all patterns - triple loop
        # 2. count pattern score
        # 3. output the top 1
        N=len(username)

        user2web=defaultdict(list)
        for ii in range(N):
            user2web[username[ii]].append((timestamp[ii], website[ii]))


        pattern2user=defaultdict(set)
        mxf=0
        mxp=[]
        for uu, vv in user2web.items():
            vv.sort()

            for ii in range(len(vv)):
                for jj in range(ii+1, len(vv)):
                    for kk in range(jj+1, len(vv)):
                        pattern=(vv[ii][1], vv[jj][1], vv[kk][1])
                        pattern2user[pattern].add(uu)
                        if len(pattern2user[pattern]) >= mxf:
                            #print(" a joined pattern: ", "".join(mxp), "".join(pattern))
                            if len(pattern2user[pattern]) == mxf:
                                if ":".join(mxp) > ":".join(pattern):
                                    mxp=pattern
                            else:
                                mxp=pattern
                                mxf=len(pattern2user[pattern])

        return mxp


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
