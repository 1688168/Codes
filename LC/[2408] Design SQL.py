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
