from collections import deque
class Node:
    def __init__(self):
        self.children={}
        self.is_word=False

class Trie:
    def __init__(self):
        self.root=Node()
        self.path2val={}

    def add(self, w):
        #print(" ===== adding ===== ")
        itr=self.root

        ww=w[1:].split('/')

        for c in ww[:-1]:
            if c not in itr.children:
                return False
            itr=itr.children[c]

        if ww[-1] in itr.children: return False
        itr.children[ww[-1]]=Node()
        itr=itr.children[ww[-1]]
        itr.is_word=True
        return True

    def is_word(self, w):
        #print(" ==== is_word =====")
        itr=self.root

        ww=w[1:].split('/')
        #print(" ww: ", ww)
        for c in ww:
            #print("c: ", c)
            if c not in itr.children:
                # print(" not in children: ")
                # print("childrens: ", itr.children)
                return False
            itr=itr.children[c]
        return itr.is_word

#     def pt(self):
#         itr=self.root

#         dq=deque([itr])

#         lvl=0
#         while sz:=len(dq) > 0:

#             for _ in range(sz):
#                 curr=dq.popleft()

#                 for kk, vv in curr.children.items():
#                     print("lvl: ", lvl, " kk: ", kk, " is_word: ", vv.is_word)
#                     dq.append(vv)

#             lvl += 1

class FileSystem:

    def __init__(self):
        self.t=Trie()



    def createPath(self, path: str, value: int) -> bool:

        if len(path)==0: return False


        if not self.t.add(path): return False
        self.t.path2val[path]=value

        #self.t.pt()
        return True

    def get(self, path: str) -> int:
        #self.t.pt()
        if self.t.is_word(path):
            return self.t.path2val[path]
        else:
            return -1



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
