class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res=[]
        wl=len(words[0])
        wc=len(words) # word count
        sl=len(s)     # string length
        cwl=wc*wl     # concatenated word length
        if wc==0 or sl==0 or wl==0: return res
        """
         barfoothefoobarma
         0 ... 9
        """
        word2cnt={}
        for w in words:
            word2cnt[w]=word2cnt.get(w,0)+1

        def is_concatenated(s):
            #print(s)
            if len(s)==0: return False
            cnt=0
            word2cnt_local=word2cnt.copy()
            for ii in range(0, len(s)-wl+1, wl):
                wi=s[ii:ii+wl]
                if wi not in word2cnt_local: return False
                cnt+=1
                word2cnt_local[wi] -=  1
                if word2cnt_local[wi]==0: del word2cnt_local[wi]
           
            return True if cnt==wc else False
            
        for ii in range(sl-cwl+1):
            if is_concatenated(s[ii:ii+cwl]): res.append(ii)

    
        return res
        
        