############################
# 20230513: 53.15%
############################
class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word=False
        self.count=0

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def is_word(self, w):
        itr = self.root
        for c in w:
            if c not in itr.children: return False
            itr=itr.children[c]

        return itr.is_word
    
    def add(self, w):
        itr=self.root
        
        for c in w:
            if c not in itr.children:
                itr.children[c]=TrieNode()
            
            itr=itr.children[c]
            itr.count += 1
        
        itr.is_word = True
    
    
    def remove(self, w):
        itr = self.root

        for c in w:
            if c not in itr.children: return
            itr = itr.children[c]
            itr.count -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        1. DFS on each word: 12X12=144
           Time: each w is 10 chars
                   there are 3X10^4 words
            : 10X3X10^4=3X10^5
            : find the starting point from the grid
            : 144*3^10^4*10*4
        2. Build Trie on word list
           DFS each cell on the board: 144 DFS, stop if the visited char is not on Trie
           Trie Depth: 10
           144*10
        """
        # build trie
        T=Trie()
        for w in words:
            T.add(w)

        # DFS each cell

        M = len(board)
        N = len(board[0])

        res=[]

        def isInScope(rr, cc):
            if rr < 0 or cc < 0: return False
            if rr >= M or cc >= N: return False
            return True

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(rr, cc, visited, tn, ww):
            if not isInScope(rr, cc): return

            curr = board[rr][cc]
            if (rr, cc) in visited: return
            if curr not in tn.children: return
            if tn.children[curr].count <=0: return
    
            visited.add((rr,cc))

            tn = tn.children[curr]
            if tn.is_word:
                res.append(ww+curr)
                tn.is_word=False
                T.remove(ww+curr)
 
            
            for dr, dc in dirs:
                nr, nc = rr+dr, cc+dc
                dfs(nr, nc, visited, tn, ww+curr)

            visited.remove((rr, cc))

        for ii in range(M):
            for jj in range(N):
                visited=set()
                ww=""
                dfs(ii, jj, visited, T.root, ww)
        
        return res
        
############################
############################

from collections import deque

class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word=False
        self.count=0


class Trie:
    def __init__(self):
        self.root=TrieNode()

    def pt(self):
        """
        : print tree
        """
        dq=deque([self.root])
        lvl=0
        while (sz:=len(dq)) > 0:
            print(" ===== ", lvl, " ===== ")
            for _ in range(sz):
                curr=dq.popleft()

                curr_node=""
                for kk, vv in curr.children.items():
                    curr_node += (kk+",")
                    dq.append(vv)
                print(" curr_node: ", curr_node, " is_word: ", curr.is_word,
                      " count: ", curr.count)
            lvl+=1

    def is_word(self, word):
        itr=self.root
        for c in word:
            if c not in itr.children:
                return False
            itr=itr.children[c]

        return itr.is_word

    def add_word(self, word):
        itr=self.root
        for c in word:
            if c not in itr.children:
                itr.children[c]=TrieNode()
            itr=itr.children[c]
            itr.count +=1
        itr.is_word=True

    def remove(self, word):
        itr=self.root
        for c in word:
            if c in itr.children:
                itr=itr.children[c]
                itr.count -=1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res=set()
        t=Trie()
        for w in words:# build the trie
            t.add_word(w)
        #t.pt() #print the trie

        M=len(board) # take the dimentions of the board
        N=len(board[0])
        dirs=[(1, 0), (-1, 0), (0, 1), (0, -1)] # options of the directions

        def is_valid(row, col):
            if row < 0 or row >= M or col < 0 or col >= N:
                return False
            return True

        def dfs(rr, cc, node, ww):

            if not is_valid(rr, cc):
                return False

            if (rr, cc) in visited: return False

            if board[rr][cc] not in node.children:
                return False

            if node.children[board[rr][cc]].count<=0: return
            #ww += board[rr][cc]
            visited.add((rr, cc))
            node=node.children[board[rr][cc]]

            if node.is_word:
                res.add(ww+board[rr][cc])
                node.is_word=False
                t.remove(ww+board[rr][cc])

            for dr, dc in dirs:
                nr, nc = rr+dr, cc+dc
                if (nr, nc) in visited: continue
                if is_valid(nr, nc):
                    #if node.count >= 0:
                    dfs(nr, nc, node, ww+board[rr][cc])

            visited.remove((rr, cc)) #back-track path

        for ii in range(M): #for all rows
            for jj in range(N): # for all cols
                ww=""
                visited=set()
                dfs(ii, jj, t.root, ww)


        return list(res)


