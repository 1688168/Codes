"""
20230501: 17%
"""

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(scores):
            tensCnt=0
            ttl=0
            for ii, ss in enumerate(scores):
                ttl += ss
                if tensCnt > 0:
                    ttl += ss
                
                if ss==10:
                    tensCnt += 1
                
                if ii-2 >=0 and scores[ii-2]==10:
                    tensCnt -= 1
            return ttl
        

        s1=score(player1)
        s2=score(player2)
        #print("s1: ", s1, " s2: ", s2)

        if s1==s2: return 0

        return 1 if s1>s2 else 2