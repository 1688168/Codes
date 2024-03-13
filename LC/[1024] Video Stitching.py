class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        """
        * interval merge
        * interval insert
        * given a list of intervals -> min to cover all

        * sort by beginning:
        * sort by ending:

        * clips[ii]=[starti, endi]: intervals (you can cut)
        => min num of clips to cover [0, time]

        * [1326]: 
         - a list of intervals (tap coverage)
         - min number of intervals to cover the entire garden watering 
        """

        """
        1. sort clips by starting time
        2. for each clip
        """
        # sort by beginning (ascending) then ending (decending)
        clips.sort(key=lambda x: (x[0], -x[1])) 

        N=len(clips)
        ii=0
        ending=0
        cnt=0
        while ii < N:
            new_ending = ending
            cnt +=1

            # find inscope clips to move ending forward for coverage
            while ii<N and clips[ii][0] <= ending:
                new_ending = max(new_ending, clips[ii][1])
                ii+=1 

            if new_ending>=time: return cnt
            if new_ending==ending: return -1
            ending=new_ending
        return -1

