"""
# the challenge is how to handle zero?
* The API only requires return the products of last K elements, we, therefore, 
do not need to persist each element.
* per above point, we only maintain the "pre-prod from last zero"
# data structure
* n: num of elements so far (API can only append) 
* preprod: product from prev-zero till current (anything prior than last zero is
irrelevant as we only care about "product of last k")
* ------------0-----k------------n
              ^
              last-zero
if range k is lass than (n-last_zero) 
-> product_k = preprod[-1]//preprod[n-k-last_zero]
"""

class ProductOfNumbers:

    def __init__(self):
        self.preprod = [1]
        self.n = 0
        self.last_zero = 0

    def add(self, num: int) -> None:

        self.n += 1

        if num == 0:
            self.preprod = [1]
            self.last_zero = self.n
        else:
            self.preprod.append(self.preprod[-1]*num)

    def getProduct(self, k: int) -> int:
        """

        n 1 2 3 4 5 6 7 8 9
        1 x x x x 0 x x x x

        last_zero=4
        k >=5: return 0
        st=9-5=4


        """
        # if self.n-k < self.last_zero: return 0
        if k <= self.n-self.last_zero:  # last k is in none-zero region
            return self.preprod[-1]//self.preprod[self.n-k-self.last_zero]
        return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
