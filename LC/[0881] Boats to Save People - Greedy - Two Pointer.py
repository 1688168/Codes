class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        ll, rr = 0, N-1
        people.sort()
        cnt = 0
        """
        1 2 2 
        """
        while ll <= rr:
            if people[ll]+people[rr] <= limit:
                ll += 1
            rr -= 1
            cnt += 1

        return cnt


######################
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        ll, rr = 0, N-1
        people.sort()
        cnt = 0
        """
        1 2 2 
        """
        while ll <= rr:
            if people[ll]+people[rr] > limit:
                rr -= 1
            else:
                ll += 1
                rr -= 1
            cnt += 1

        return cnt
