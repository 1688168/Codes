class TextEditor:

    def __init__(self):
        self.stk0 = []
        self.stk1 = []

    def addText(self, text: str) -> None:
        for c in text:
            self.stk0.append(c)

    def deleteText(self, k: int) -> int:
        cnt = 0
        while self.stk0 and k > 0:
            self.stk0.pop()
            k -= 1
            cnt += 1
        return cnt

    def cursorLeft(self, k: int) -> str:
        while self.stk0 and k > 0:
            self.stk1.append(self.stk0.pop())
            k -= 1
        """
        k=2
        len=4
        abcd
        """
        idx = max(0, len(self.stk0)-10)
        return "".join(self.stk0[idx:])

    def cursorRight(self, k: int) -> str:
        while self.stk1 and k > 0:
            self.stk0.append(self.stk1.pop())
            k -= 1

        idx = max(0, len(self.stk0)-10)
        return "".join(self.stk0[idx:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
