import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    # Ініціалізуємо екземпляр калькулятора перед кожним тестом
    return Calculator()

def test_add(calculator):
    assert calculator.add(3, 5) == 8
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2

def test_subtract(calculator):
    assert calculator.subtract(10, 5) == 5
    assert calculator.subtract(-1, -1) == 0
    assert calculator.subtract(-1, 1) == -2

def test_multiply(calculator):
    assert calculator.multiply(3, 5) == 15
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(-1, -1) == 1

def test_parse_input_invalid(calculator):
    # Перевірка неправильного введення
    with pytest.raises(ValueError):
        calculator.parse_input("2+1")

    with pytest.raises(ValueError):
        calculator.parse_input("2_1")

    with pytest.raises(ValueError):
        calculator.parse_input("abc")

    with pytest.raises(ValueError):
        calculator.parse_input("12a")

    with pytest.raises(ValueError):
        calculator.parse_input("!@#")

    with pytest.raises(ValueError):
        calculator.parse_input("")

    with pytest.raises(ValueError):
        calculator.parse_input("3.14.15")

    assert calculator.parse_input("3") == 3

def test_divide(calculator):
    assert calculator.divide(10, 2) == 5
    # Перевірка винятку при діленні на нуль
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
