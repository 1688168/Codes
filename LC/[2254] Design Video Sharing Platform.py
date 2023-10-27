video_rec = namedtuple('video_rec', ['video', 'like', 'dislike', 'cnt'])


class VideoSharingPlatform:
    """
    - video[i]: video content @ minute i
    - video[i]: (content, like, dislike, num_of_views)

    - videoId: the smallest available id, from zeroq1q
    """

    def __init__(self):
        self.mnh = []   # mean heap
        self.mx_vid = 0  # max videoId as of now starting from zero
        self.vid2video = {}

    def upload(self, video: str) -> int:
        if self.mnh:  # to return the min vid
            videoId = heapq.heappop(self.mnh)
        else:
            videoId = self.mx_vid
            self.mx_vid += 1
        self.vid2video[videoId] = video_rec(
            video, 0, 0, 0)  # [string,likes,dislikes,views]
        return videoId

    def remove(self, videoId: int) -> None:
        if videoId not in self.vid2video:
            return
        heapq.heappush(self.mnh, videoId)
        del self.vid2video[videoId]

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId in self.vid2video:
            rec = self.vid2video[videoId]  # increment view count
            new_rec = video_rec(rec.video, rec.like, rec.dislike, rec.cnt+1)
            self.vid2video[videoId] = new_rec
            s = rec.video  # video content
            # do not return exceeding video length
            return s[startMinute:min(endMinute+1, len(s))]
        return '-1'

    def like(self, videoId: int) -> None:
        if videoId in self.vid2video:
            rec = self.vid2video[videoId]  # increment view count
            new_rec = video_rec(rec.video, rec.like+1,
                                rec.dislike, rec.cnt)  # increment like
            self.vid2video[videoId] = new_rec

    def dislike(self, videoId: int) -> None:
        if videoId in self.vid2video:
            rec = self.vid2video[videoId]  # increment view count
            new_rec = video_rec(rec.video, rec.like,
                                rec.dislike+1, rec.cnt)  # increment dislike
            self.vid2video[videoId] = new_rec

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        return self.vid2video[videoId][1:3] if videoId in self.vid2video else [-1]

    def getViews(self, videoId: int) -> int:
        return self.vid2video[videoId].cnt if videoId in self.vid2video else -1
######################################################


class VideoSharingPlatform:

    def __init__(self):
        self.h = []
        self.mx = 0
        self.vid = {}

    def upload(self, video: str) -> int:
        if self.h:
            videoId = heapq.heappop(self.h)
        else:
            videoId = self.mx
            self.mx += 1
        self.vid[videoId] = [video, 0, 0, 0]  # [string,likes,dislikes,views]
        return videoId

    def remove(self, videoId: int) -> None:
        if videoId not in self.vid:
            return
        heapq.heappush(self.h, videoId)
        del self.vid[videoId]

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId in self.vid:
            self.vid[videoId][3] += 1
            s = self.vid[videoId][0]
            return s[startMinute:min(endMinute+1, len(s))]
        return '-1'

    def like(self, videoId: int) -> None:
        if videoId in self.vid:
            self.vid[videoId][1] += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.vid:
            self.vid[videoId][2] += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        return self.vid[videoId][1:3] if videoId in self.vid else [-1]

    def getViews(self, videoId: int) -> int:
        return self.vid[videoId][3] if videoId in self.vid else -1
