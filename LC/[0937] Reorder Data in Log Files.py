class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)


###########
# 20230916
###########

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_row = []
        letter_row = []

        for row in logs:
            lrow = row.split(" ")
            if lrow[1].isnumeric():
                digit_row.append(row)
            else:
                letter_row.append(row)

        def my_sort(row):
            rowl = row.split(" ")
            return (" ".join(rowl[1:]), rowl[0])
        letter_row.sort(key=my_sort)

        return letter_row+digit_row
