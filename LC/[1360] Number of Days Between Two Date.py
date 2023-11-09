################
# 2023108
################
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """
        diff of two days = abs(diff(day1, 1971) - diff(day2, 1971)) 
        """

        def is_leap_year(year):

            if year % 4 != 0:
                return False
            elif year % 100 != 0:
                return True
            elif year % 400 != 0:
                return False
            else:
                return True

        def leaps(yy, mm):
            cnt = 0
            for yr in range(1971, yy):
                if is_leap_year(yr):
                    cnt += 1
            if is_leap_year(yy) and mm > 2:
                cnt += 1
            return cnt

        def get_days(date):
            yy, mm, dd = map(int, date.split("-"))
            leap_cnt = leaps(yy, mm)
            mo = [0, 31, 28, 31, 30, 31, 30, 31, 31,
                  30, 31, 30, 31]  # this starts from zero

            return leap_cnt + (yy-1971)*365+sum(mo[:mm])+dd

        return abs(get_days(date2)-get_days(date1))


################################
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
