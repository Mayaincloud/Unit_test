import pytest
from mean_value import MeanValue
from compare import CompareMean


# Mean
# проверка что это список, а не "другое"
def test_invalid_type_exception():
    with pytest.raises(TypeError):
        MeanValue('string')

# проверка передачи в список  не чисел
def test_invalid_elem_exception():
    with pytest.raises(ValueError):
        MeanValue([1, 2, "string"])

# проверка правильности вычисления среднего значения
def test_average_calc():
    avg = MeanValue([1, 2, 3, 4])
    assert avg.get_mean() == 2.5

# проверка равности списков
def test_equal_avg():
    avg1 = MeanValue([1, 2, 3, 4])
    avg2 = MeanValue([1, 2, 3, 4])
    assert avg1 == avg2

# проверка сравнения средних значений списков
def test_avg1_great_avg2():
    avg1 = MeanValue([5, 6, 7, 8])
    avg2 = MeanValue([1, 2, 3, 4])
    assert avg1 > avg2

# проверка сравнения средних значений списков
def test_avg1_less_avg2():
    avg1 = MeanValue([1, 2, 3, 4])
    avg2 = MeanValue([5, 6, 7, 8])
    assert avg1 < avg2

# проверка сравнения средних значений списков
def test_equal_averages():
    avg1 = MeanValue([1, 2, 3, 4])
    avg2 = MeanValue([2, 2, 3, 3])
    assert avg1 == avg2

# проверка сравнения средних значений списков
def test_less_than_average():
    avg1 = MeanValue([1, 1, 1, 1])
    avg2 = MeanValue([2, 2, 2, 2])
    assert avg1 < avg2
    assert not avg1 > avg2

# проверка расчета среднего значения пустого списка
def test_empty_list_avg():
    avg = MeanValue([])
    assert avg.get_mean() == 0.0

# проверка свойства
def test_lst_property():
    lst = [1, 2, 3]
    avg = MeanValue(lst)
    assert avg.lst == lst


# проверка сравнение значений CompareMean

def test_comp_avg1_great_avg2():
    avg1 = MeanValue([5, 6, 7, 8])
    avg2 = MeanValue([1, 2, 3, 4])
    comp = CompareMean(avg1, avg2)
    assert comp.compare_mean() == "Среднее значение первого списка больше"

# проверка сравнение значений CompareMean
def test_comp_avg1_less_avg2():
    avg1 = MeanValue([1, 2, 3, 4])
    avg2 = MeanValue([5, 6, 7, 8])
    comp = CompareMean(avg1, avg2)
    assert comp.compare_mean() == "Среднее значение второго списка больше"

# проверка сравнение значений CompareMean
def test_second_list_has_great_avg():
    avg1 = MeanValue([1, 2, 3, 4])
    avg2 = MeanValue([5, 6, 7, 8, 9])
    comp = CompareMean(avg1, avg2)
    assert comp.compare_mean() == "Среднее значение второго списка больше"

# проверка сравнение значений CompareMean
def test_comp_equal_avg():
    avg1 = MeanValue([1, 2, 3, 4])
    avg2 = MeanValue([1, 2, 3, 4])
    comp = CompareMean(avg1, avg2)
    assert comp.compare_mean() == "Списки имеют равные средние значения"

# проверка свойства класса
def test_comp_mean_properties():
    avg1 = MeanValue([1, 2, 3])
    avg2 = MeanValue([4, 5, 6])
    comp = CompareMean(avg1, avg2)
    assert comp.mean_1 == avg1
    assert comp.mean_2 == avg2


# Запускаем тесты
pytest.main(["-v"])
