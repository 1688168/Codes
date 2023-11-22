from abc import ABC, abstractclassmethod



class IWinStrategy(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def get_winner(self, a, b, c):
        pass


class Annihilation(IWinStrategy):
    def __init__(self, a, b, c):
        super().__init__(a)
        