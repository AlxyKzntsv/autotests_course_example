import pytest
import datetime


@pytest.fixture(autouse=True)
def tests_timing():
    start = datetime.datetime.now()
    print()
    yield
    end = datetime.datetime.now()
    print((f'Прохождение тестов началось в {start}, завершилось в {end}'))



@pytest.fixture()
def test_time():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    time = end - start
    print(f'Время выполнения теста {time}')