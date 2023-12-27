class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TextEditor:
    def __init__(self):
        self.cursor = Node(-1)

    def addText(self, text: str) -> None:
        curr = self.cursor
        last = curr.right
        for c in text:
            curr.right = Node(c)
            curr.right.left = curr
            curr = curr.right
        curr.right = last
        if last:
            last.left = curr
        self.cursor = curr

    def deleteText(self, k: int) -> int:
        curr = self.cursor
        last = curr.right
        tot = 0
        while k and curr.val != -1:
            curr = curr.left
            k -= 1
            tot += 1
        if last:
            last.left = curr
        curr.right = last
        self.cursor = curr
        return tot

    def cursorLeft(self, k: int) -> str:
        while k and self.cursor.val != -1:
            self.cursor = self.cursor.left
            k -= 1
        return self.getvals(self.cursor)

    def cursorRight(self, k: int) -> str:
        while k and self.cursor.right:
            self.cursor = self.cursor.right
            k -= 1
        return self.getvals(self.cursor)

    def getvals(self, curr):
        vals = deque()
        k = 10
        while k and curr.val != -1:
            vals.appendleft(curr.val)
            curr = curr.left
            k -= 1
        return "".join(vals)
