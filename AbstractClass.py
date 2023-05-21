from abc import ABC, abstractmethod


class Mobile(ABC):
    @abstractmethod
    def calling(self):
        pass

    @abstractmethod
    def messaging(self):
        pass


class Oneplus(Mobile):
    def calling(self):
        print("Oneplus can call")

    def messaging(self):
        print("Oneplus can sent message")


class Samsung(Mobile):
    def calling(self):
        print("Samsung can call")

    def messaging(self):
        print("Samsung can sent message")


op = Oneplus()
op.calling()
op.messaging()
