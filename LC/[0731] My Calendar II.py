"""
Tripple booking:
1. find all events that has intersection with new events into a list
2. is there

"""
class MyCalendarTwo:

    def __init__(self):
        self.events=[]


    def book(self, start: int, end: int) -> bool:
        def is_triple_booked(st, ed):
            self.events.sort()

            conflicts=[]
            ns, ne = start, end
            #collect all events that has conflict with new event
            for cs, ce in self.events:
                if not (ne <= cs or ns >=ce):
                    conflicts.append((cs, ce))

                if cs >= ne: break

            # for all collected conflicts, is there conflict btn any pair?

            if len(conflicts) > 0:
                ns, ne = conflicts[0]

                for cs, ce in conflicts[1:]:
                    if not (ne <= cs or ns >= ce): return True
                    ns, ne=cs, ce

            return False

        
        if not is_triple_booked(start, end):
            self.events.append((start, end))
            return True

        return False


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
