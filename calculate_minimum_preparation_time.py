from abc import abstractmethod, ABC


class FactoryCalculateMinimumPreparationTime(ABC):

    @abstractmethod
    def execute(self, **kwargs):
        pass


class CalculateMinimumPreparationTime(FactoryCalculateMinimumPreparationTime):

    def execute(self, **kwargs):
        return {
            'class': type(self)
        }


class CalculateMinimumPreparationTimeOld(FactoryCalculateMinimumPreparationTime):

    def execute(self, **kwargs):
        return {
            'class': type(self)
        }
