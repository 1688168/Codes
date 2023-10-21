class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        r1 = self.get_days(date1)
        r2 = self.get_days(date2)
        return abs(r2 - r1)

    def leapyear(self, year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    def get_days(self, a_str):
        s = a_str.split('-')
        year, month, day = map(int, s)
        n_leaps = 0
        for i in range(1971, year):
            n_leaps += int(self.leapyear(i))
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 32]
        res = n_leaps + 365 * (year - 1971) + sum(months[:month]) + day
        if self.leapyear(year) and month > 2:
            res += 1
        return res
