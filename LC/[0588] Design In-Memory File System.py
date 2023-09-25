##########
# 20230924
##########
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_file = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, ws, is_file):
        if ws is None or len(ws) == 0:
            return

        itr = self.root
        for w in ws:
            if w not in itr.children:
                itr.children[w] = TrieNode()

            itr = itr.children[w]

        if is_file:
            itr.is_file = True


class FileSystem:

    def __init__(self):
        self.file2content = {}
        self.trie = Trie()

    def ls(self, path: str) -> List[str]:
        tkns = path[1:].split("/")
        itr = self.trie.root
        for tkn in tkns:
            if tkn in itr.children:
                itr = itr.children[tkn]

        if itr.is_file:
            return [tkn]
        else:
            return sorted([kk for kk in itr.children.keys()])

    def mkdir(self, path: str) -> None:
        self.trie.add(path[1:].split("/"), False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.trie.add(filePath[1:].split("/"), True)
        self.file2content[filePath] = self.file2content.get(
            filePath, "") + content

    def readContentFromFile(self, filePath: str) -> str:
        return self.file2content[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)


##########
# 20221102
##########
class Node:
    def __init__(self):
        self.children = {}
        self.is_file = False


class FileSystem:

    def __init__(self):
        self.root = Node()
        self.path2content = {}

    def ls(self, path: str) -> List[str]:
        itr = self.root

        tkns = path[1:].split("/")
        for t in tkns:
            if t in itr.children:
                itr = itr.children[t]
            else:
                print(" ls a null directory?")

        if itr.is_file:
            return [t]
        else:
            return sorted([kk for kk in itr.children.keys()])

    def mkdir(self, path: str) -> None:
        itr = self.root

        tkns = path[1:].split("/")
        for t in tkns:
            if t not in itr.children:
                itr.children[t] = Node()
            itr = itr.children[t]

    def addContentToFile(self, filePath: str, content: str) -> None:
        itr = self.root

        tkns = filePath[1:].split("/")
        for t in tkns:
            if t not in itr.children:
                itr.children[t] = Node
            itr = itr.children[t]

        itr.is_file = True
        self.path2content[filePath] = self.path2content.get(
            filePath, "") + content

    def readContentFromFile(self, filePath: str) -> str:

        return self.path2content.get(filePath, "")


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

####################################################################
####################################################################
class Node:
    def __init__(self):
        self.children = {}  # key=substr of the path, value=children
        self.is_file = False


class FileSystem:

    def __init__(self):
        self.root = Node()
        self.path2content = {}

    def ls(self, path: str) -> List[str]:
        itr = self.root
        tokens = path[1:].split("/")
        # print("ls tokens: ", tokens)
        for tkn in tokens:
            if tkn in itr.children:
                # itr.children[tkn]=Node()
                itr = itr.children[tkn]

        if itr.is_file == True:
            return [tkn]
        else:
            res = [kk for kk in itr.children.keys()]
            res.sort()
            # print("ls res: ", res)
            return res

    def mkdir(self, path: str) -> None:
        itr = self.root
        tkns = path[1:].split("/")
        for tkn in tkns:
            if tkn not in itr.children and tkn != '':
                itr.children[tkn] = Node()
            itr = itr.children[tkn]
        return

    def addContentToFile(self, filePath: str, content: str) -> None:
        itr = self.root
        tkns = filePath[1:].split("/")
        for tkn in tkns:
            if tkn not in itr.children:
                itr.children[tkn] = Node()
            itr = itr.children[tkn]
        itr.is_file = True
        self.path2content[filePath] = self.path2content.get(
            filePath, "") + content

    def readContentFromFile(self, filePath: str) -> str:
        return self.path2content.get(filePath, "")


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
