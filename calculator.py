class Calculator:
    def add (self, a, b):
        return a + b
    def subtract (self, a, b):
        return a - b
    def multiply (self, a, b):
        return a * b
    def divide (self, a, b):
        if b == 0:
            raise ValueError("Не можна ділити на нуль")
        return a / b

    def parse_input(self, input_str):

        # Перевірка на зайву кількість десяткових крапок
        if input_str.count('.') > 1:
            raise ValueError("Число не може містити більше однієї десяткової крапки")
        # Перевірка на порожній рядок
        if input_str.strip() == "":
            raise ValueError("Вхідне значення не може бути порожнім")

        # Перевірка на наявність символів, які не є числами або коректними форматами
        if not input_str.replace('.', '', 1).isdigit() and not (
                input_str[0] == '-' and input_str[1:].replace('.', '', 1).isdigit()):
            raise ValueError("Неправильний формат виразу")

        return float(input_str)
