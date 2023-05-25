import abc


class Food(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_nutrition(self) -> float:
        raise NotImplemented
