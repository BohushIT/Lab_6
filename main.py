from calculator import Calculator

def main():
    calculator = Calculator()

    print("Консольний Калькулятор")
    print("Введіть два числа та виберіть операцію:")

    try:
        # Отримуємо числа від користувача та перевіряємо їх на правильний формат
        a_input = input("Введіть перше число: ")
        a = calculator.parse_input(a_input)

        b_input = input("Введіть друге число: ")
        b = calculator.parse_input(b_input)

        # Вибір операції
        print("\nВиберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")

        operation = input("Введіть номер операції (1/2/3/4): ")

        # Словник операцій
        operations = {
            '1': calculator.add,
            '2': calculator.subtract,
            '3': calculator.multiply,
            '4': calculator.divide
        }

        # Отримуємо функцію з словника та викликаємо її
        if operation in operations:
            result = operations[operation](a, b)
            print(f"Результат: {result}")
        else:
            print("Невірний вибір операції. Спробуйте ще раз.")

    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()

    # Очистка покриття coverage erase
    # Створення покриття coverage run -m pytest
    #coverage run -m unittest discover
    # Створення звіту
    #coverage html -d coverage_html_report
    # coverage run -m unittest TestCalculator.py



