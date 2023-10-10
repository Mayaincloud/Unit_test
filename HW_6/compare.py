from mean_value import MeanValue


class CompareMean:

    def __init__(self, mean_1: MeanValue, mean_2: MeanValue):
        self._mean_1 = mean_1
        self._mean_2 = mean_2

    @property
    def mean_1(self):
        return self._mean_1

    @property
    def mean_2(self):
        return self._mean_2

    def compare_mean(self):
        if self._mean_1 > self._mean_2:
            return f"Среднее значение первого списка больше"
        elif self._mean_1 < self._mean_2:
            return f"Среднее значение второго списка больше"
        else:
            return f"Списки имеют равные средние значения"