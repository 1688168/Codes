class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        """
        keys: unique chars
        values: len(values[ii])=2
        dictionary: permitted original string for encryption
        """
        self.k2v = {k: v for k, v in zip(keys, values)}

        self.permitted_encrypts = collections.defaultdict(int)
        for w in dictionary:
            encrypted_w = self.encrypt(w)
            if encrypted_w == "":
                continue
            self.permitted_encrypts[encrypted_w] += 1

    def encrypt(self, word1: str) -> str:
        """
        return "" if key is not existing
        """
        res = ""
        for cc in word1:
            if cc not in self.k2v:
                return ""
            res += self.k2v[cc]

        return res

    def decrypt(self, word2: str) -> int:
        """
        return cnt
        """
        # be careful word2 might not be in permitted_encrypts
        return self.permitted_encrypts[word2] if word2 in self.permitted_encrypts else 0


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
