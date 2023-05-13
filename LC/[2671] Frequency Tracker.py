"""
20230511: 
T: 7.78%

"""
class FrequencyTracker:

    def __init__(self):
        self.arr=[0]*100001
        self.v2f={}
        

    def add(self, number: int) -> None:
        if number in self.v2f:
            self.arr[self.v2f[number]] -=1
        self.v2f[number] = self.v2f.get(number,0)+1
        self.arr[self.v2f[number]]+=1

    def deleteOne(self, number: int) -> None:
        if number in self.v2f:
            self.arr[self.v2f[number]]-=1
            self.v2f[number] -=1
            self.arr[self.v2f[number]] +=1
        
            if self.v2f[number]==0:
                del self.v2f[number]
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.arr[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)