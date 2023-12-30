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
        self.stk = []
        self.nxt = None
        for ii in reversed(range(len(nestedList))):
            self.stk.append(nestedList[ii])

    def next(self) -> int:
        val = self.nxt
        self.nxt = None
        return val

    def hasNext(self) -> bool:
        if not self.stk:
            return False

        while self.stk:
            o = self.stk.pop()
            if o.isInteger():
                self.stk.append(o.getInteger())
                break
            ol = o.getList()
            for ii in reversed(range(len(ol))):
                self.stk.append(ol[ii])
        if self.stk:
            self.nxt = self.stk.pop()
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
