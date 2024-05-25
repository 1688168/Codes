class Codec:
    def __init__(self, _counter=0):
        self.mm={}
        self.counter=_counter
        
    def encode(self, longUrl: str) -> str:
        self.counter += 1
        key="www.tinyurl.com/"+ str(self.counter)
        print("key: ", key)
        self.mm[key]=longUrl
        return key
        
    def decode(self, shortUrl: str) -> str:
        print("shortUrl: ", shortUrl)
        if shortUrl in self.mm:
            return self.mm[shortUrl]
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))