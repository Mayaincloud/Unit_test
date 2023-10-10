from __future__ import annotations


class MeanValue:

    def __init__(self, lst: list[int | float]):
        if not isinstance(lst, list):
            raise TypeError('Argument must be a list type')
        for item in lst:
            if not isinstance(item, (int, float)):
                raise ValueError(f'Element {item} not int or float')
        self._lst = lst

    @property
    def lst(self):
        return self._lst

    def get_mean(self) -> float:
        if len(self._lst):
            return sum(self._lst) / len(self._lst)
        return 0.0

    def __eq__(self, other):
        return self.get_mean() == other.get_mean()

    def __gt__(self, other):
        return self.get_mean() > other.get_mean()

    def __lt__(self, other):
        return self.get_mean() < other.get_mean()