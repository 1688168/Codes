# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def generator(nl):
            for ll in nl:
                if ll.isInteger():
                    yield ll.getInteger()
                else:
                    yield from generator(ll.getList())

        self.nxt = None
        self.gen = generator(nestedList)

    def next(self) -> int:
        o = None
        if self.hasNext():
            o, self.nxt = self.nxt, None
        return o

    def hasNext(self) -> bool:
        if self.nxt is not None:
            return True

        try:
            self.nxt = next(self.gen)
            return True
        except:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
