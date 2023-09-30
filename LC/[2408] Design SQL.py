###################
# 20230930
###################
from collections import defaultdict


class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tbl2row = defaultdict(list)

    def insertRow(self, name: str, row: List[str]) -> None:
        self.tbl2row[name].append(row)

    def deleteRow(self, name: str, rowId: int) -> None:
        self.tbl2row[name][rowId-1] = None

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tbl2row[name][rowId-1][columnId-1]

################################
################################


class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {name: [] for name in names}

    def insertRow(self, name: str, row: List[str]) -> None:
        self.tables[name].append(row)

    def deleteRow(self, name: str, rowId: int) -> None:
        # we could simpy `pass` this, but this releases the memory that was allocated for the deleted row
        self.tables[name][rowId - 1] = None

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name][rowId - 1][columnId - 1]
