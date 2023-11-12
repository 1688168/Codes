from sortedcontainers import SortedList


class SORTracker:

    def __init__(self):
        self.scores = SortedList()
        self.i = 0

    def add(self, name: str, score: int) -> None:
        self.scores.add((-score, name))

    def get(self) -> str:
        self.i += 1
        return self.scores[self.i - 1][1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
