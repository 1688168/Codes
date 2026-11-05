class Solution:
    def nextClosestTime(self, time: str) -> str:
        HH = int(time[:2])
        MM = int(time[-2:])

        digits=set(time)
        while True:
            MM += 1
            if MM >= 60:
                HH+=1
                MM=0
                HH=HH%24

            TT=f"""{HH:02d}:{MM:02d}"""
            s1=set(TT)
            if s1 <= digits: return TT
        
        return time
        